from rest_framework import serializers
from api.models import MouvementPlace

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MouvementPlace
        fields = '__all__'