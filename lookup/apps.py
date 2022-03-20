#Author: nicolas.diez.risueno@gmail.com
#Project: Weather Lookup App (w/ Django)

from django.apps import AppConfig


class LookupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lookup'
