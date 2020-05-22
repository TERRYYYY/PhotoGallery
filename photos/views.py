from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
# Create your views here.

def index(request):
    return render(request, 'index.html')

def my_photos(request):
    date = dt.date.today()
    return render(request, 'all-photos/gallery.html', {"date": date,})