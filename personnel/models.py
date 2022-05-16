from django.db import models

from societe.models import Societe
from mail.models import Mail
from accounts.models import Account

# Create your models here.

class Agence(models.Model):
    nom_agence = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_agence

class Personnel(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    stagiaire = models.BooleanField()
    diffusion = models.CharField(max_length=5)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True)
    societe_id = models.ForeignKey(Societe, on_delete=models.PROTECT)
    agence_id = models.ForeignKey(Agence, on_delete=models.PROTECT)
    isactif = models.BooleanField()

    def __str__(self):
        return self.nom


class PersonnelNote(models.Model):
    personnel_id = models.ForeignKey(Personnel, on_delete=models.PROTECT)
    write_by_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    write_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True)


class Rpm(models.Model):
    personnel_id = models.ForeignKey(Personnel, on_delete=models.PROTECT)
    mail_id = models.ForeignKey(Mail, on_delete=models.PROTECT)


class TypeCompte(models.Model):
    nom_type = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_type


class Compte(models.Model):
    personnel_id = models.ForeignKey(Personnel, on_delete=models.PROTECT)
    type_compte_id = models.ForeignKey(TypeCompte, on_delete=models.PROTECT)
    login = models.CharField(max_length=30)
    default_pwd = models.CharField(max_length=30)
    lien_site = models.CharField(max_length=255)
    isactif = models.BooleanField(null=True)