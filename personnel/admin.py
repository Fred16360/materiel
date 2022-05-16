from django.contrib import admin

from .models import Compte, Personnel, PersonnelNote, TypeCompte, Rpm

# Register your models here.

class PersonnelAdmin(admin.ModelAdmin):
    model = Personnel
    list_display = ['nom', 'prenom', 'societe_id']
    
admin.site.register(Personnel, PersonnelAdmin)


class PersonnelNoteAdmin(admin.ModelAdmin):
    model = PersonnelNote
    list_display = ['personnel_id', 'write_by_id', 'write_date', 'note']

admin.site.register(PersonnelNote, PersonnelNoteAdmin)


class RpmAdmin(admin.ModelAdmin):
    model = Rpm
    list_display = ['personnel_id', 'mail_id']

admin.site.register(Rpm, RpmAdmin)


class TypeCompteAdmin(admin.ModelAdmin):
    model = TypeCompte
    list_display = ['nom_type']

admin.site.register(TypeCompte, TypeCompteAdmin)


class CompteAdmin(admin.ModelAdmin):
    model = Compte
    list_display=['personnel_id', 'type_compte_id']

admin.site.register(Compte, CompteAdmin)