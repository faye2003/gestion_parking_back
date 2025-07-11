from rest_framework import serializers
from api.models import Vehicule

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'