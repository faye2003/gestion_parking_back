from rest_framework import serializers
from api.models import Utilisateur
from django.contrib.auth.hashers import make_password

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

def create(self, validated_data):
    # Hachage du mot de passe si fourni
    if 'password' in validated_data and validated_data['password']:
        validated_data['password'] = make_password(validated_data['password'])
    return super().create(validated_data)