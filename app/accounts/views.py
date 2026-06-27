from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    """Render the home page"""
    return HttpResponse("Welcome to the Home Page of the Recipe API App!")