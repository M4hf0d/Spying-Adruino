from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('gps', GpsPointViewSet, basename='gps')
router.register('data', DataViewSet, basename='data')
router.register('journey', JourneyViewSet, basename = 'journey')
urlpatterns = [
    path('geomap/', geomap_context, name='geomap'),
    path('map/', home, name='map' ),
    path('lastgps/', LastGpsPointView.as_view(), name='last-gps-point'),
] + router.urls

