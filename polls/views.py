import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer


@api_view(['GET'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.filter().order_by('pub_date')[:5]
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)


def question_detail(request, pk):

    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        choices = Choice.objects.filter(question=question).order_by('choice_text')
        serializer = ChoiceSerializer(choices, many=True)
        res = {
            'question': question.question_text,
            'choices': serializer.data
        }
        return JsonResponse(res, safe=False)


def question_result(request, pk):

    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    choices = Choice.objects.filter(question=question).order_by('-votes')
    serializer = ChoiceSerializer(choices, many=True)
    res = {
        'question': question.question_text,
        'choices': serializer.data
    }
    return JsonResponse(res, safe=False)

@api_view(['POST'])
def vote(request, pk):

    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)

    try:

        data = JSONParser().parse(request)
        selected_choice = question.choice_set.get(pk=data['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse(status=404)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponse(status=201)
