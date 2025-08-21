from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.paiement_viewset import PaiementViewSet

router = DefaultRouter()
router.register(r'paiement', PaiementViewSet, basename='paiement')

urlpatterns = router.urls
