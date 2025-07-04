# Generated by Django 5.1.7 on 2025-06-18 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ip_address', models.GenericIPAddressField()),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(choices=[('ADMIN', 'Admin'), ('SUPERVISEUR', 'Superviseur'), ('CLIENT', 'Client')], max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypePaiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('total_places', models.PositiveIntegerField()),
                ('statut', models.BooleanField(default=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('localite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.localite')),
            ],
        ),
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('nb_vehicules', models.PositiveIntegerField()),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.camera')),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parking')),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='parking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parking'),
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=255)),
                ('localite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.localite')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('montant', models.FloatField()),
                ('statut', models.CharField(choices=[('EN_ATTENTE', 'En attente'), ('PAYE', 'Payé'), ('ANNULE', 'Annulé'), ('ECHOUE', 'Échoué')], default='EN_ATTENTE', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type_paiement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.typepaiement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('type', models.CharField(choices=[('SMS', 'SMS'), ('EMAIL', 'Email')], max_length=10)),
                ('objet', models.CharField(max_length=100)),
                ('statut', models.CharField(choices=[('ENVOYEE', 'Envoyée'), ('ECHOUEE', 'Échouée')], default='ENVOYEE', max_length=10)),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_client', models.CharField(max_length=20, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('solde', models.FloatField(default=0)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('type_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.typeaccount')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('immatricule', models.CharField(max_length=50, unique=True)),
                ('couleur', models.CharField(max_length=50)),
                ('parking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.parking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure_entree', models.DateTimeField(blank=True, null=True)),
                ('heure_sortie', models.DateTimeField(blank=True, null=True)),
                ('statut', models.CharField(choices=[('LIBRE', 'Libre'), ('OCCUPEE', 'Occupée')], default='LIBRE', max_length=10)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parking')),
                ('vehicule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.vehicule')),
            ],
        ),
    ]
