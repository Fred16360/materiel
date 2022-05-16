from django.db import models
from django.db.models.fields import DateField

from accounts.models import Account
from personnel.models import Personnel

# Create your models here.
class TypeEquipement(models.Model):
    nom_type = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_type


class Marque(models.Model):
    nom_marque = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_marque


class Modele(models.Model):
    nom_modele = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_modele


class Seller(models.Model):
    seller_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.seller_name


class Equipement(models.Model):
    sig_id = models.CharField(max_length=30, unique=True)
    type_id = models.ForeignKey(TypeEquipement, on_delete=models.PROTECT)
    marque = models.ForeignKey(Marque, on_delete=models.PROTECT)
    modele = models.ForeignKey(Modele, on_delete=models.PROTECT)
    num_serie = models.CharField(max_length=30, null=True)
    detail = models.TextField()
    seller_id = models.ForeignKey(Seller, on_delete=models.PROTECT, null=True)
    buy_date = models.DateField(null=True)
    guarantee_end_date = models.DateField(null=True)
    mac_addr1 = models.CharField(max_length=30)
    mac_addr2 = models.CharField(max_length=30)

    def __str__(self):
        return self.sig_id


class EquipementNote(models.Model):
    equipement_id = models.ForeignKey(Equipement, on_delete=models.PROTECT)
    write_by_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    write_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True)


class Ripe(models.Model):
    ip_machine = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=30, null=True)
    equipement_id = models.ForeignKey(Equipement, on_delete=models.PROTECT, null=True)


class Rpe(models.Model):
    personnel_id = models.ForeignKey(Personnel, on_delete=models.PROTECT)
    equipement_id = models.ForeignKey(Equipement, on_delete=models.PROTECT)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)