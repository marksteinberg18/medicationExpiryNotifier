from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def testFunction(request): 
    return HttpResponse('Hello World')

def test2Function(request): 
    return HttpResponse('Hello World number 2')