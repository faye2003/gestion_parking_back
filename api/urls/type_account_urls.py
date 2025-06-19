from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.type_account_viewset import TypeAccountViewSet

router = DefaultRouter()
router.register(r'type-account', TypeAccountViewSet, basename='typeaccount')

urlpatterns = router.urls
