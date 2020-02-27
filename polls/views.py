from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, world. You are at the poll index')

def detail(request, question_id):
    return HttpResponse('You are looking at question %s. '% question_id)

def result(request, question_id):
    response = "You're are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question % s. " % question_id)