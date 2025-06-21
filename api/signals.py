from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Profil

@receiver(post_migrate)
def create_default_profiles(sender, **kwargs):
    for role in ['ADMIN', 'SUPERVISEUR', 'CLIENT']:
        Profil.objects.get_or_create(libelle=role)
