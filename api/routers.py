from django.urls import path, include
from api.urls.utilisateur_urls import urlpatterns as utilisateur_urls
from api.urls.type_account_urls import urlpatterns as type_account_urls
from api.urls.type_paiement_urls import urlpatterns as type_paiement_urls
from api.urls.localite_urls import urlpatterns as localite_urls
from api.urls.profil_urls import urlpatterns as profil_urls
from api.urls.parking_urls import urlpatterns as parking_urls
from api.urls.place_urls import urlpatterns as place_urls
from api.urls.vehicule_urls import urlpatterns as vehicule_urls
from api.urls.paiement_urls import urlpatterns as paiement_urls
from api.urls.dashboard_urls import urlpatterns as dashboard_urls
from api.urls.contact_urls import urlpatterns as contact_urls
from api.urls.views_urls import urlpatterns as views_urls

urlpatterns = [
    path('api/', include(utilisateur_urls)),
    path('api/', include(type_account_urls)),
    path('api/', include(type_paiement_urls)),
    path('api/', include(localite_urls)),
    path('api/', include(profil_urls)),
    path('api/', include(parking_urls)),
    path('api/', include(place_urls)),
    path('api/', include(vehicule_urls)),
    path('api/', include(paiement_urls)),
    path('api/', include(dashboard_urls)),
    path('api/', include(contact_urls)),
    path('api/', include(views_urls)),
]
