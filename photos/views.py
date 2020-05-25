from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Image, Location ,Category
# Create your views here.

# def index(request):
#     return render(request, 'index.html')

def index(request):
    date = dt.date.today()
    images = Image.get_images()
    location = Location.get_location()
    locations = Location.get_location()

    return render(request, 'all-photos/images.html', {"date": date, "images": images, "location": location, "locations": locations})
    