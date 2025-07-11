from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.serializers.place_serializer import PlaceSerializer
from api.pagination import CustomPagination
from django.utils import timezone

from api.models import Vehicule, MouvementPlace, Place


@api_view(['POST'])
def detecter_entree_sortie(request):
    immatricule = request.data.get("immatricule")
    if not immatricule:
        return Response({"error": "Immatricule manquant"}, status=400)

    vehicule = Vehicule.objects.filter(immatricule=immatricule).first()

    if not vehicule:
        return Response({"error": "Véhicule non enregistré"}, status=404)

    place_occupee = Place.objects.filter(vehicule=vehicule, statut='OCCUPEE').first()

    if place_occupee:
        # Sortie
        place_occupee.heure_sortie = timezone.now()
        place_occupee.statut = 'LIBRE'
        place_occupee.vehicule = None
        place_occupee.save()

        MouvementPlace.objects.filter(vehicule=vehicule, place=place_occupee, date_sortie__isnull=True).update(date_sortie=timezone.now())

        return Response({"message": "Sortie enregistrée"}, status=200)
    else:
        # Entrée
        place_libre = Place.objects.filter(statut='LIBRE').first()
        if not place_libre:
            return Response({"error": "Aucune place libre disponible"}, status=400)

        place_libre.heure_entree = timezone.now()
        place_libre.statut = 'OCCUPEE'
        place_libre.vehicule = vehicule
        place_libre.save()

        MouvementPlace.objects.create(
            vehicule=vehicule,
            place=place_libre,
            date_entree=timezone.now()
        )

        return Response({"message": "Entrée enregistrée", "place_id": place_libre.id}, status=200)
