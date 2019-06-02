from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def MyApplicationView(request):
    return HttpResponse("<h1>Welcome to Macc Family</h1>")
