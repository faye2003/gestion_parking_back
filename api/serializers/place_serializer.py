from rest_framework import serializers
from api.models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['parking'] = {
            'id': instance.parking.id,
            'libelle': instance.parking.libelle
        }
        return rep