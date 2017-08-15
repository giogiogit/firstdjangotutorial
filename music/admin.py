from django.contrib import admin
from .models import Album, Song

# to add Album into the admin zone
admin.site.register(Album)
admin.site.register(Song)

