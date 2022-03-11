# Views.py file is the one which handles http requests and drives them to the corresponding html webpage
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})