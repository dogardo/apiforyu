from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def howto(request):
    return render(request,"howto.html")