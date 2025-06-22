from django.urls import path, include
from api.urls.utilisateur_urls import urlpatterns as utilisateur_urls
from api.urls.type_account_urls import urlpatterns as type_account_urls
from api.urls.type_paiement_urls import urlpatterns as type_paiement_urls
from api.urls.localite_urls import urlpatterns as localite_urls
from api.urls.profil_urls import urlpatterns as profil_urls
from api.urls.parking_urls import urlpatterns as parking_urls

urlpatterns = [
    path('api/', include(utilisateur_urls)),
    path('api/', include(type_account_urls)),
    path('api/', include(type_paiement_urls)),
    path('api/', include(localite_urls)),
    path('api/', include(profil_urls)),
    path('api/', include(parking_urls)),
]
