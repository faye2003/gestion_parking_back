from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.place_viewset import PlaceViewSet

router = DefaultRouter()
router.register(r'place', PlaceViewSet, basename='place')

urlpatterns = router.urls
