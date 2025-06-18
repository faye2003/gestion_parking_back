from rest_framework.routers import DefaultRouter
from api.viewset.utilisateur_viewset import UtilisateurViewSet

router = DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
urlpatterns = router.urls
