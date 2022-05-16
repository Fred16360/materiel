from django.contrib import admin

from .models import Mail, HebergeurMail, ConfigMail
# Register your models here.

class HebergeurMailAdmin(admin.ModelAdmin):
    model = HebergeurMail
    list_display = ['nom_hebergeur']

admin.site.register(HebergeurMail, HebergeurMailAdmin)


class ConfigMailAdmin(admin.ModelAdmin):
    model = ConfigMail
    list_display = ['nom_societe', 'hebergeur_mail_id']

admin.site.register(ConfigMail, ConfigMailAdmin)


class MailAdmin(admin.ModelAdmin):
    model = Mail
    list_display = ['compte_mail', 'password', 'alias']

admin.site.register(Mail, MailAdmin)