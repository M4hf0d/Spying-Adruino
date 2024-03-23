from django.contrib import admin
from .models import GPSData, Data

# Register your models here.

admin.site.register(GPSData)
admin.site.register(Data)