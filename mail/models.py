from django.db import models

from societe.models import Societe
# Create your models here.

class HebergeurMail(models.Model):
    nom_hebergeur = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_hebergeur


class ConfigMail(models.Model):
    nom_societe = models.ForeignKey(Societe, on_delete=models.PROTECT)
    hebergeur_mail_id = models.ForeignKey(HebergeurMail, on_delete=models.PROTECT)
    protocole = models.CharField(max_length=10)
    srv_entrant = models.CharField(max_length=30)
    login_srv_entrant = models.CharField(max_length=30)
    pwd_srv_entrant = models.CharField(max_length=30)
    port_srv_entrant = models.IntegerField()
    srv_sortant = models.CharField(max_length=30)
    login_srv_sortant = models.CharField(max_length=30)
    pwd_srv_sortant = models.CharField(max_length=30)
    ssl_or_other = models.CharField(max_length=10)
    authentification = models.CharField(max_length=20)
    port_srv_sortant = models.IntegerField()

    def __str__(self):
        return str(self.nom_societe) + ' (' + str(self.protocole) + ')'


class Mail(models.Model):
    compte_mail = models.EmailField(max_length=255)
    password = models.CharField(max_length=30)
    alias = models.CharField(max_length=255)
    config_mail_id = models.ForeignKey(ConfigMail, null=True, on_delete=models.PROTECT)
    etat = models.CharField(max_length=50)
    nbr_utilisation = models.IntegerField(null=True)
    capacite = models.IntegerField(null=True)
    mo_go = models.CharField(max_length=3)
    commentaire = models.TextField()

    def __str__(self):
        return self.compte_mail

