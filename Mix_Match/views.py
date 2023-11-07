from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def Mix_Match(request):
    template = loader.get_template('flavors.html')
    res = template.render()
    return HttpResponse(res)

def feature(request):
    flavors=['chocolate','vanilla','strawberry']
    
