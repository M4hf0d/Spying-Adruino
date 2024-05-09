from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('gps', GpsPointViewSet, basename='gps')
router.register('data', DataViewSet, basename='data')

urlpatterns = router.urls
