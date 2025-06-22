from rest_framework import serializers
from api.models import Parking

class ParkingSerializer(serializers.ModelSerializer):
    localite = serializers.CharField(source='localite.libelle', read_only=True)
    total_places = serializers.SerializerMethodField()
    places_libres = serializers.SerializerMethodField()
    places_occupees = serializers.SerializerMethodField()

    class Meta:
        model = Parking
        fields = '__all__'

    def get_total_places(self, obj):
        return obj.places.count()

    def get_places_libres(self, obj):
        return obj.places.filter(statut='Libre').count()

    def get_places_occupees(self, obj):
        return obj.places.filter(statut='Occupee').count()