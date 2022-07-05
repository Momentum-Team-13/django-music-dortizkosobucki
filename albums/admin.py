from django.contrib import admin
from .models import Album, Favorite

# Register your models here.
admin.site.register(Album)
admin.site.register(Favorite)