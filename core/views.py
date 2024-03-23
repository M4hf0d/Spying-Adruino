from django.shortcuts import render
from rest_framework import generics
from .models import GPSData,Data
from .serializers import GPSDataSerializer,DataSerializer

class GPSDataListCreateView(generics.ListCreateAPIView):
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer

class DataListCreateView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer