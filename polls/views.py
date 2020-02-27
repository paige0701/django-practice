from django.core import serializers
from django.http import HttpResponse

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.filter().order_by('-pub_date')[:5]
    data = serializers.serialize('json', latest_question_list, )
    return HttpResponse(data)

def detail(request, question_id):
    return HttpResponse('You are looking at question %s. '% question_id)

def result(request, question_id):
    response = "You're are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question % s. " % question_id)