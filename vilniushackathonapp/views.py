from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from vilniushackathon import urls
# For API environment keys
from django.conf import settings


def home(request):
    return HttpResponse("Hello, Django!")

def index(request):
    return render(request, "index.html")

def map(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, "map.html")

