import requests
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from vilniushackathon import urls
# For API environment keys
from django.conf import settings

# For redirection
from django.shortcuts import render, redirect


def home(request):
    return HttpResponse("Hello, Django!")

def index(request):
    return render(request, "index.html")

def find_container(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        # Logic to find green containers near the provided address
        # You can pass this data to the template or redirect
        return render(request, 'results.html', {'address': address})
    else:
        return redirect('index')

def map(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, "map.html")

# Taking data from Vilnius Open data and display as a table
def greenwaste(request):
    # URL of the JSON API
    url = 'https://gis.vplanas.lt/arcgis/rest/services/Interaktyvus_zemelapis/Miesto_tvarkymas/MapServer/87/query?where=1%3D1&f=pjson&outFields=*'

    #Fetch data from the API
    response = requests.get(url)
    data = response.json()

    # Extract the relevant fields
    features = data.get('features', [])
    data_list = [feature['attributes'] for feature in features]  # Extract 'attributes' from each feature

    # Pass the data to the template
    return render(request, 'greenwaste.html', {'data_list': data_list})