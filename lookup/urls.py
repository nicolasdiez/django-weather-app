from django.urls import path
from . import views

urlpatterns = [
    #el path está vacio xq es la home ppal, de ahí colgaran el resto de webpages, ej: /about.html
    path('', views.home, name="home"),

    path('about.html', views.about, name="about"),

]
