from django.contrib.gis import admin
from .models import WorldBorder
from geodjango.models import Profile
from django.contrib.gis.db import models

class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'last_location']
    readonly_fields = ['last_location']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(WorldBorder, admin.OSMGeoAdmin)