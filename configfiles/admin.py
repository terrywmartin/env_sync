from django.contrib import admin

from .models import ConfigFile, File, Location
# Register your models here.
admin.site.register(ConfigFile)
admin.site.register(File)
admin.site.register(Location)
