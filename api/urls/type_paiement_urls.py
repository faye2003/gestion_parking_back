from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.type_paiement_viewset import TypePaiementViewSet

router = DefaultRouter()
router.register(r'type-paiement', TypePaiementViewSet, basename='typepaiement')

urlpatterns = router.urls
