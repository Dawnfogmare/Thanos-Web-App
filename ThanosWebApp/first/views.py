from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def tapped_view(request):
    return HttpResponse("Hello, world. You're at boppy central.")
