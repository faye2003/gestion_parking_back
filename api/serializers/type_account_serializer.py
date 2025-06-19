from rest_framework import serializers
from api.models import TypeAccount

class TypeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAccount
        fields = '__all__'