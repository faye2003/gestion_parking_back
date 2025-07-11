from django.db import models

from django.utils import timezone
# Create your models here.

class Localite(models.Model):
    libelle = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Profil(models.Model):
    libelle = models.CharField(max_length=50, unique=True)

class Utilisateur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    localite = models.ForeignKey(Localite, on_delete=models.SET_NULL, null=True)

class Parking(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    # total_places = models.PositiveIntegerField()
    statut = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    localite = models.ForeignKey(Localite, on_delete=models.SET_NULL, null=True)
    

class Camera(models.Model):
    nom = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    actif = models.BooleanField(default=True)

class Detection(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    nb_vehicules = models.PositiveIntegerField()
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

class Vehicule(models.Model):
    immatricule = models.CharField(max_length=50, unique=True)
    marque = models.CharField(max_length=100, null=True, blank=True)
    couleur = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.immatricule

class Place(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name='places')
    vehicule = models.ForeignKey('Vehicule', on_delete=models.SET_NULL, null=True, blank=True)
    heure_entree = models.DateTimeField(null=True, blank=True)
    heure_sortie = models.DateTimeField(null=True, blank=True)

    STATUT_CHOICES = [
        ('LIBRE', 'Libre'),
        ('OCCUPEE', 'Occupée'),
    ]
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='LIBRE')

    def __str__(self):
        return f"Place {self.id} - {self.statut}"

    @property
    def duree_stationnement(self):
        if self.heure_entree and self.heure_sortie:
            return self.heure_sortie - self.heure_entree
        return None

    def occuper(self, vehicule):
        """Méthode pour occuper une place"""
        self.vehicule = vehicule
        self.heure_entree = timezone.now()
        self.statut = 'OCCUPEE'
        self.save()

    def liberer(self):
        """Méthode pour libérer une place"""
        self.heure_sortie = timezone.now()
        self.statut = 'LIBRE'
        self.vehicule = None
        self.save()

class MouvementPlace(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date_entree = models.DateTimeField()
    date_sortie = models.DateTimeField(null=True, blank=True)



class TypeAccount(models.Model):
    libelle = models.CharField(max_length=100)

class Account(models.Model):
    libelle = models.CharField(max_length=100)
    solde = models.FloatField(default=0)
    date_modification = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    type_account = models.ForeignKey(TypeAccount, on_delete=models.SET_NULL, null=True)

class TypePaiement(models.Model):
    libelle = models.CharField(max_length=100)

class Paiement(models.Model):
    description = models.CharField(max_length=255)
    montant = models.FloatField()
    statut = models.CharField(
        max_length=20,
        choices=[('EN_ATTENTE', 'En attente'), ('PAYE', 'Payé'), ('ANNULE', 'Annulé'), ('ECHOUE', 'Échoué')],
        default='EN_ATTENTE'
    )
    date = models.DateTimeField(auto_now_add=True)
    type_paiement = models.ForeignKey(TypePaiement, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Contact(models.Model):
    numero_client = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)

class Notification(models.Model):
    message = models.TextField()
    type = models.CharField(
        max_length=10,
        choices=[('SMS', 'SMS'), ('EMAIL', 'Email')]
    )
    objet = models.CharField(max_length=100)
    statut = models.CharField(
        max_length=10,
        choices=[('ENVOYEE', 'Envoyée'), ('ECHOUEE', 'Échouée')],
        default='ENVOYEE'
    )
    date_envoi = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)
