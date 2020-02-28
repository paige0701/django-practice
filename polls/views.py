from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from polls.models import Question
from polls.serializers import QuestionSerializer


def index(request):
    latest_question_list = Question.objects.filter().order_by('-pub_date')[:5]
    serializer = QuestionSerializer(latest_question_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def detail(request, question_id):
    return HttpResponse('You are looking at question %s. '% question_id)

def result(request, question_id):
    response = "You're are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question % s. " % question_id)