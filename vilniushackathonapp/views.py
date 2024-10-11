from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from vilniushackathon import urls


def home(request):
    return HttpResponse("Hello, Django!")

