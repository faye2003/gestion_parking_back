from rest_framework import serializers
from api.models import Parking
from api.models import Localite
from api.models import Place
from api.serializers.place_serializer import PlaceSerializer
from api.serializers.localite_serializer import LocaliteSerializer

class ParkingSerializer(serializers.ModelSerializer):
    localite_id = serializers.PrimaryKeyRelatedField(
        queryset=Localite.objects.all(), source='localite', write_only=True
    )
    localite = LocaliteSerializer(read_only=True) 
    total_places = serializers.SerializerMethodField()
    places_libres = serializers.SerializerMethodField()
    places_occupees = serializers.SerializerMethodField()
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Parking
        fields = '__all__'

    def get_total_places(self, obj):
        return obj.places.count()

    def get_places_libres(self, obj):
        return obj.places.filter(statut='Libre').count()

    def get_places_occupees(self, obj):
        return obj.places.filter(statut='Occupee').count()