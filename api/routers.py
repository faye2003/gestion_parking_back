from django.urls import path, include
from api.urls.utilisateur_urls import urlpatterns as utilisateur_urls
from api.urls.type_account_urls import urlpatterns as type_account_urls

urlpatterns = [
    path('api/', include(utilisateur_urls)),
    path('api/', include(type_account_urls)),
]
