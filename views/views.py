from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

def funky(request):
    response = """<html><body><p>This is the funky function sample</p>
    </body></html>"""
    return HttpResponse(response)
