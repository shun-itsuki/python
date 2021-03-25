from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world this is index page")