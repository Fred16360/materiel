from equipement.forms import EquipementNoteForm
from django.contrib import admin
from django.db import models

from .models import TypeEquipement, Marque, Modele, Seller, Equipement, EquipementNote, Ripe, Rpe

# Register your models here.
class TypeEquipementAdmin(admin.ModelAdmin):
    model = TypeEquipement
    list_display = ['nom_type']

admin.site.register(TypeEquipement, TypeEquipementAdmin)


class MarqueAdmin(admin.ModelAdmin):
    model = Marque
    list_display = ['nom_marque']

admin.site.register(Marque, MarqueAdmin)


class ModeleAdmin(admin.ModelAdmin):
    model = Modele
    list_display = ['nom_modele']

admin.site.register(Modele, ModeleAdmin)


class SellerAdmin(admin.ModelAdmin):
    model = Seller
    list_display = ['seller_name']

admin.site.register(Seller, SellerAdmin)


class EquipementAdmin(admin.ModelAdmin):
    model = Equipement
    list_display = ['sig_id', 'type_id', 'marque', 'modele', 'buy_date', 'guarantee_end_date', 'mac_addr1']

admin.site.register(Equipement, EquipementAdmin)


class RipeAdmin(admin.ModelAdmin):
    model = Ripe
    list_display = ['ip_machine', 'equipement_id', 'description']

admin.site.register(Ripe, RipeAdmin)


class RpeAdmin(admin.ModelAdmin):
    model = Rpe
    list_display = ['personnel_id', 'equipement_id', 'date_debut', 'date_fin']

admin.site.register(Rpe, RpeAdmin)


class EquipementNoteAdmin(admin.ModelAdmin):
    model : EquipementNote
    list_display = ['equipement_id', 'write_by_id', 'write_date', 'note']

admin.site.register(EquipementNote, EquipementNoteAdmin)