from rest_framework import serializers
from api.models import TypePaiement

class TypePaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePaiement
        fields = '__all__'