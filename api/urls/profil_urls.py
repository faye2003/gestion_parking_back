from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.profil_viewset import ProfilViewSet

router = DefaultRouter()
router.register(r'profil', ProfilViewSet, basename='profil')

urlpatterns = router.urls
