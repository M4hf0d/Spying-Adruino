from .views import *
from django.urls import path



urlpatterns = [
 path('gps/', GPSDataListCreateView.as_view(), name='gps'),
    path('data/', DataListCreateView.as_view(), name='data'),
]
