from django.shortcuts import render
from rest_framework import generics
from .models import GPSData
from .serializers import GPSDataSerializer

class GPSDataListCreateView(generics.ListCreateAPIView):
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer