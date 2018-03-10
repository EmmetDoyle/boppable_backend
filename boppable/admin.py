from django.contrib import admin

# Register your models here.
from boppable.models import *

admin.site.register(User)
admin.site.register(Party)
admin.site.register(Playlist)
admin.site.register(TrackVoting)