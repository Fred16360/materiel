from django.db import models

# Create your models here.

class Societe(models.Model):
    nom_societe = models.CharField(max_length=20)
    siret = models.CharField(max_length=30)
    ape = models.CharField(max_length=20)
    nom_gerant = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_societe