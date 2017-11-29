from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Context, loader
from django.views.decorators.csrf import csrf_exempt
from api.models import Question
import random


def app_root(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

    #return HttpResponse("<html><title>Hi</title><h1>suckittrebek</h1></html>")
@csrf_exempt
def display_random_question(request):
    #template = loader.get_template('jon.html')
    #do something here that gets a random question
    all_questions = len(Question.objects.all())
    rnd_question_id = random.randint(1,all_questions)
    question_entry = Question.objects.get(pk=rnd_question_id)
    #goulet = 9
    return HttpResponse("<html><title>Booties</title><h1>Word: "+ str(question_entry.question) + "</h1><h2>Definition: " + str(question_entry.definition) + "</h2><h3>Example: " + str(question_entry.example) + "</h3></html>")

#I added this b/c when I was attempting to get to this path, it was freaking the fuck out
@csrf_exempt
def display_question(request):
    template = loader.get_template('jon.html')
    return HttpResponse(template.render())
