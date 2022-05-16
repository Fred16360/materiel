from django.forms import ModelForm, fields
from django import forms
    
from .models import Mail, ConfigMail, Societe, HebergeurMail


class MailForm(forms.ModelForm):
    MOGO_CHOIX = [
        ('MO', 'Mo'),
        ('GO', 'Go')
    ]
    class Meta:
        model = Mail
        fields ='__all__'

    compte_mail = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    password = forms.CharField(
        label='Mot de passe',
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    alias = forms.CharField(
        label='Alias',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    config_mail_id = forms.ModelChoiceField(
        queryset=ConfigMail.objects.all(),
        label='Configuration Mail',
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    etat = forms.CharField(
        label='Etat',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    nbr_utilisation = forms.IntegerField(
        label='Nombre d''utilisation',
        required=False,
        widget=forms.NumberInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    capacite = forms.IntegerField(
        label='Capacité',
        required=False,
        widget=forms.NumberInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    mo_go = forms.ChoiceField(
        choices=MOGO_CHOIX,
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    commentaire = forms.CharField(
        label='Commentaire',
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": "5",
            "cols": "25",
        })
    )


class ConfigMailForm(forms.ModelForm):
    PROTOCOLE_CHOIX = [
        ('IMAP', 'IMAP'),
        ('POP', 'POP')
    ]
    SSL_CHOIX = [
        ('NO', 'Aucune'),
        ('STTLS', 'STARTTLS'),
        ('SSL', 'SSL/TLS')
    ]
    AUTH_CHOIX = [
        ('MDPTNS', 'Mot de passe (transmission non sécurisée'),
        ('MDPC', 'Mot de passe chiffré'),
        ('GSS', 'Kerberos/GSSAPI'),
        ('NTLM', 'NTLM'),
        ('AUTH2', 'Auth2')
    ]
    class Meta:
        model = ConfigMail
        fields = '__all__'

    nom_societe = forms.ModelChoiceField(
        queryset=Societe.objects.all(),
        label='Nom de la société',
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    hebergeur_mail_id = forms.ModelChoiceField(
        queryset=HebergeurMail.objects.all(),
        label='Hébergeur',
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    protocole = forms.ChoiceField(
        choices=PROTOCOLE_CHOIX,
        label='Protocole',
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    srv_entrant = forms.CharField(
        label='Serveur entrant',
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    login_srv_entrant = forms.CharField(
        label='Login serveur entrant',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    pwd_srv_entrant = forms.CharField(
        label='Mot de passe',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    port_srv_entrant = forms.IntegerField(
        label='Port serveur entrant',
        required=True,
        widget=forms.NumberInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    srv_sortant = forms.CharField(
        label='Serveur entrant',
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    login_srv_sortant = forms.CharField(
        label='Login serveur entrant',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    pwd_srv_sortant = forms.CharField(
        label='Mot de passe',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    port_srv_sortant = forms.IntegerField(
        label='Port serveur sortant',
        required=True,
        widget=forms.NumberInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    ssl_or_other = forms.ChoiceField(
        choices=SSL_CHOIX,
        label='Sécurité de la connexion',
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    authentification = forms.ChoiceField(
        choices=AUTH_CHOIX,
        label='Authentification',
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    

class HebergeurMailForm(forms.ModelForm):
    class Meta:
        model = HebergeurMail
        fields = '__all__'

    nom_hebergeur = forms.CharField(
        label='Nom de l``hébergeur',
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )

'''    


    hebergeur_id = forms.ModelChoiceField(
        queryset=HebergeurMail.objects.all(),
        label='Hébergeur',
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    societe_id = forms.ModelChoiceField(
        queryset=Societe.objects.all(),
        label='Société',
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    alias = forms.CharField(
        label='Alias',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    capacite = forms.IntegerField(
        label='Capacité',
        required=False,
        widget=forms.NumberInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


    blackberry = forms.CharField(
        label='Blackberry',
        required=False,
        widget=forms.Textarea(attrs={
            "rows": "3",
            "class": "form-control"
        })
    )
'''

