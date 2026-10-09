from django.shortcuts import render
from django.https import HttpResponse

def home(request):
    return HttpResponse("Hello munjya")
    

# Create your views here.
