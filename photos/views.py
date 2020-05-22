from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
# Create your views here.

def index(request):
    return render(request, 'index.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-photos/gallery.html', {"date": date,})