from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Context, loader


def app_root(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

    #return HttpResponse("<html><title>Hi</title><h1>suckittrebek</h1></html>")
