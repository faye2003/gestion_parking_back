from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.contact_viewset import ContactViewSet

router = DefaultRouter()
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = router.urls
