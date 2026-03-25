from django.contrib import admin

from .models import  Genre,Track,genre_track

admin.site.register(Genre)
admin.site.register(genre_track)
admin.site.register(Track)
# Register your models here.
