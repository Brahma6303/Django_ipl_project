from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def msd(request):
    return render(request,'msd.html')

def rutraj(request):
    return HttpResponse("<h1><center>Rutraj is the captin of csk</center></h1>")