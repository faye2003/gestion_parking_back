from django.urls import path, include
from api.urls.utilisateur_urls import urlpatterns as utilisateur_urls

urlpatterns = [
    path('api/', include(utilisateur_urls)),
]
