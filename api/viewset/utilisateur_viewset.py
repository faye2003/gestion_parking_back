from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Utilisateur
from api.pagination import CustomPagination
from api.serializers.utilisateur_serializer import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['prenom', 'nom', 'email']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'status': True,
                'message': 'Liste récupérée avec succès',
                'data': serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': True,
            'message': 'Liste récupérée avec succès',
            'data': serializer.data
        })


    def create(self, request, *args, **kwargs):
        print("🔥 create() appelé avec:", request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'status': True,
                'message': 'Utilisateur créé avec succès',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': 'Erreur lors de la création',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                'status': True,
                'message': 'Utilisateur mis à jour avec succès',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': 'Erreur lors de la mise à jour',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status': True,
            'message': 'Utilisateur supprimé avec succès'
        }, status=status.HTTP_200_OK)


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
