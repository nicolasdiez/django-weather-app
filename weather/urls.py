#Author: nicolas.diez.risueno@gmail.com
#Project: Weather Lookup App (w/ Django)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lookup.urls')),
]
