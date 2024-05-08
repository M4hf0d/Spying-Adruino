from rest_framework import generics,viewsets
from .models import GPSData,Data
from .serializers import GPSDataSerializer,DataSerializer

class GPSDataViewSet(viewsets.ModelViewSet):
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer