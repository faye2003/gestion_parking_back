from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.parking_viewset import ParkingViewSet

router = DefaultRouter()
router.register(r'parking', ParkingViewSet, basename='parking')

urlpatterns = router.urls
