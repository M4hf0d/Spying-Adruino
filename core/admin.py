from django.contrib import admin
from .models import GpsPoint, Data


@admin.register(GpsPoint)
class GpsPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'latitude', 'longitude', 'timestamp']
    list_filter = ('timestamp',)
    date_hierarchy = 'timestamp'



admin.site.register(Data)