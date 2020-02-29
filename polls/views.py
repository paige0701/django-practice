import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer


def index(request):
    latest_question_list = Question.objects.filter().order_by('-pub_date')[:5]
    serializer = QuestionSerializer(latest_question_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def detail(request, question_id):
    qu = Question.objects.filter(id=question_id).first()
    choices = Choice.objects.filter(question=qu).all()
    s = ChoiceSerializer(choices, many=True)
    res = {
        'question': qu.question_text,
        'choices': s.data
    }
    return JsonResponse(res, safe=False)

def result(request, question_id):
    response = "You're are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        body = json.loads(request.body)
        selected_choice = question.choice_set.get(pk=body['choice'])
    except (KeyError, Choice.DoesNotExist):
        return Response(None, 404)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponse('Success')
