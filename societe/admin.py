from django.contrib import admin

from .models import Societe
# Register your models here.

class SocieteAdmin(admin.ModelAdmin):
    model = Societe
    list_display = ['nom_societe', 'siret', 'ape', 'nom_gerant']

admin.site.register(Societe, SocieteAdmin)