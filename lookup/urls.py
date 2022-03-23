# Author: nicolas.diez.risueno@gmail.com
# Project: Weather Lookup App (w/ Django)

from django.urls import path
from . import views

urlpatterns = [
    
    #Home.html - el path está vacio xq es la home ppal, de ahí colgaran el resto de webpages, ej: /about.html
    path('', views.home, name="home"),

    #About.html
    path('about.html', views.about, name="about"),

]
