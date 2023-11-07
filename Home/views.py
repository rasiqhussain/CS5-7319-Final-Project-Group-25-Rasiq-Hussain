from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    res = template.render()
    return HttpResponse(res)

def image(request):
    template = loader.get_template('image-1.jpg')
    res = template.render()
    return HttpResponse(res)