from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def testFunction(request): 
    test2Function(request)
    return HttpResponse('<h1>Hello World number 1</h1>')


def test2Function(request): 
    return HttpResponse('<h1>Hello World number 2</h1>')

