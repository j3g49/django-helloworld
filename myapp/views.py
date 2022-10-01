from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import requests

# Create your views here.

def index(request):
    return render(request,'index.json')

#    template = loader.get_template('myapp/index.json')
#   context = {}
#    return HttpResponse(template.render(context,request))
#    return HttpResponse("Hello World Jayathri")
