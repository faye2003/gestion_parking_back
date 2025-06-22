from rest_framework.routers import DefaultRouter
from api.viewset.utilisateur_viewset import UtilisateurViewSet

router = DefaultRouter()
router.register(r'users', UtilisateurViewSet, basename='utilisateur')
urlpatterns = router.urls
