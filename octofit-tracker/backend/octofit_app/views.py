from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the OctoFit Tracker!")

# Create your views here.
