from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context, loader
from django.views.decorators.csrf import csrf_exempt
from api.models import Question
import random
import logging

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)
logger = logging.getLogger('django.template')

def app_root(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
def display_random_question(request):
    #template = loader.get_template('jon.html')
    #do something here that gets a random question
    all_questions = len(Question.objects.all())
    rnd_question_id = random.randint(1,all_questions)
    question_entry = Question.objects.get(pk=rnd_question_id)
    my_template = loader.get_template('question_answer.html')
    #parms = Context({'question_entry.question':question_entry.question,'question_entry.definition': question_entry.definition})
    #parms = {'question_entry.question': question_entry.question,'question_entry.definition': question_entry.definition}
    parms = {'question_entry': question_entry}
    print(parms)
    #logger.info("Template name: {}".format(my_template.name))
    logger.info("Word: {}".format(question_entry.question))
    logger.info("Jons Definition: {}".format(question_entry.definition))
    print(question_entry.definition)
    #return HttpResponse(template.render(parms, request))
    #return template.render(params)
    #return render_to_response(template,parms)
    #return HttpResponse(my_template.render(parms))
    return HttpResponse(loader.render_to_string('question_answer.html',parms))
    #return HttpResponse("<html><title>Booties</title><h1>Word: " + str(question_entry.question) + "</h1><h2>Definition: " + str(question_entry.definition) + "</h2><h3>Example: " + str(question_entry.example) + "</h3></html>")

#I added this b/c when I was attempting to get to this path, it was freaking the fuck out
@csrf_exempt
def display_question(request):
    template = loader.get_template('jon.html')
    return HttpResponse(template.render())
