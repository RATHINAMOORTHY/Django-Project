from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

def MyApplicationView(request):
    return HttpResponse("<h1>Welcome to Macc Family</h1>")

def My_Very_First_Timer(request):
    CurrentTime = datetime.datetime.now()
    TimerString = "<h1>The Current Time Is : "+ str(CurrentTime) + "</h1>"
    return HttpResponse(TimerString)
