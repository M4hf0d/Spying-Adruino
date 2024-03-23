from django.shortcuts import render
from rest_framework import generics
from .models import GPSData,Data
from .serializers import GPSDataSerializer,DataSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class GPSDataListCreateView(generics.ListCreateAPIView):
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer

@csrf_exempt
class DataListCreateView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer