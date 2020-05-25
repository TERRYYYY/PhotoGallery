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

def search_images(request):
  locations = Location.get_location()
  if 'keyword' in request.GET and request.GET["keyword"]:
    search_term = request.GET.get("keyword")
    searched_images = Image.search_by_category(search_term)
    message = f"{search_term}"

    return render(request, 'all-photos/search.html', {"message": message, "images": searched_images, "locations": locations})

  else:
    message = "Invalid Search"
    return render(request, 'all-photos/search.html', {"message": message, "locations": locations})  