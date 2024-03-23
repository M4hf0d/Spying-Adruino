from .views import *
from django.urls import path



urlpatterns = [
 path('gps/', GPSDataListCreateView.as_view(), name='gps'),
]
