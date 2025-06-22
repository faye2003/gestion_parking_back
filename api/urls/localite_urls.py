from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.localite_viewset import LocaliteViewSet

router = DefaultRouter()
router.register(r'localite', LocaliteViewSet, basename='localite')

urlpatterns = router.urls
