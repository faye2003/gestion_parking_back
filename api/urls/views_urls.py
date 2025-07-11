from rest_framework.routers import DefaultRouter
from django.urls import path
from api.viewset.views import detecter_entree_sortie

router = DefaultRouter()


urlpatterns = [
    path('detecter-entree-sortie/', detecter_entree_sortie),  # 🔥 Ajoute ça ici
]
