from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.vehicule_viewset import VehiculeViewSet

router = DefaultRouter()
router.register(r'vehicule', VehiculeViewSet, basename='vehicule')

urlpatterns = router.urls
