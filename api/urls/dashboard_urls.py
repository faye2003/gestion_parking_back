from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.dashboard_viewset import DashboardViewSet

router = DefaultRouter()
router.register(r'dashboard', DashboardViewSet, basename='dashboard')

urlpatterns = router.urls
