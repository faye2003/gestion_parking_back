from rest_framework import serializers
from api.models import Utilisateur
from django.contrib.auth.hashers import make_password
from api.serializers.profil_serializer import ProfilSerializer

class UtilisateurSerializer(serializers.ModelSerializer):
    profils = ProfilSerializer(many=True, read_only=True)

    class Meta:
        model = Utilisateur
        fields = '__all__'

def create(self, validated_data):
    # Hachage du mot de passe si fourni
    if 'password' in validated_data and validated_data['password']:
        validated_data['password'] = make_password(validated_data['password'])
    return super().create(validated_data)

def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['profil'] = {
            'id': instance.profil.id,
            'nom': instance.profil.libelle
        }
        return rep