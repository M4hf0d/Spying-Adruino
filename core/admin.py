from django.contrib import admin
from .models import GpsPoint, Data, Journey
from django_admin_geomap import ModelAdmin as GeoModelAdmin

@admin.register(GpsPoint)
class GpsPointAdmin(GeoModelAdmin):
    geomap_field_longitude = "id_longitude"
    geomap_field_latitude = "id_latitude"
    geomap_autozoom = "30"
    list_display = ['id', 'latitude', 'longitude', 'timestamp']
    list_filter = ('timestamp','journey',)
    ordering = ['timestamp', 'id' ,'journey']
    date_hierarchy = 'timestamp'



admin.site.register(Data)

class GpsPointInline(admin.TabularInline):  # or admin.StackedInline if you prefer
    model = GpsPoint
    extra = 0  # Number of extra forms to display


@admin.register(Journey)
class GpsPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_point', 'end_point', 'start_time', 'end_time', 'total_distance','average_speed','duration','max_speed']
    list_filter = ('start_time','end_time',)
    date_hierarchy = 'start_time'
    inlines = [GpsPointInline]