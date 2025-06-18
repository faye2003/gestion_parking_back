from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Utilisateur
from api.serializers.utilisateur_serializer import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    @action(detail=True, methods=['post'])
    def activer(self, request, pk=None):
        utilisateur = self.get_object()
        utilisateur.profil.libelle = 'CLIENT'
        utilisateur.save()
        return Response({'status': 'Utilisateur activé'})

    @action(detail=True, methods=['post'])
    def desactiver(self, request, pk=None):
        utilisateur = self.get_object()
        utilisateur.profil.libelle = 'INACTIF'
        utilisateur.save()
        return Response({'status': 'Utilisateur désactivé'})
