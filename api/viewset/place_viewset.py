from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.serializers.place_serializer import PlaceSerializer
from api.pagination import CustomPagination

from api.models import Place


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['numero']

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
                'message': 'Place créé avec succès',
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
                'message': 'Place mis à jour avec succès',
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
            'message': 'Type de compte supprimé avec succès'
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def entree(self, request, pk=None):
        place = self.get_object()
        if place.statut == 'OCCUPEE':
            return Response({'status': False, 'message': 'La place est déjà occupée'}, status=400)

        vehicule_id = request.data.get('vehicule_id')
        if not vehicule_id:
            return Response({'status': False, 'message': 'ID du véhicule requis'}, status=400)

        try:
            vehicule = Vehicule.objects.get(id=vehicule_id)
        except Vehicule.DoesNotExist:
            return Response({'status': False, 'message': 'Véhicule introuvable'}, status=404)
        
        if Place.objects.filter(vehicule=vehicule, statut='OCCUPEE').exists():
            return Response({'status': False, 'message': 'Ce véhicule est déjà sur une place occupée'}, status=400)

        place.occuper(vehicule)
        return Response({'status': True, 'message': 'Entrée enregistrée'})

    
    @action(detail=True, methods=['post'])
    def sortie(self, request, pk=None):
        place = self.get_object()
        if place.statut == 'LIBRE':
            return Response({'status': False, 'message': 'La place est déjà libre'}, status=400)

        place.liberer()
        return Response({'status': True, 'message': 'Sortie enregistrée'})


