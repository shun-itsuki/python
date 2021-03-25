from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpRedponse("Hello world this is index page")