from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return render(request,"virat.html")

def karthik(request):
    return HttpResponse("<h1><center>Karthik is vice captin of rcb</center></h1>")