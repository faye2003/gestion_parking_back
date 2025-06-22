from rest_framework import serializers
from api.models import Localite

class LocaliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localite
        fields = ['id', 'libelle', 'latitude', 'longitude']