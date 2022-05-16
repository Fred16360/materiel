from django.forms import ModelForm, models
from django import forms
from django.forms.fields import CharField
    
from .models import PersonnelNote, Societe, Mail, Personnel, Agence, TypeCompte, Compte, Rpm

class PersonnelForm(forms.ModelForm):
    DIFFUSION_CHOIX = [
            ('OUI', 'Oui'),
            ('NON', 'Non')
    ]
    class Meta:
        model = Personnel
        fields = '__all__'
               
    nom = forms.CharField(
        required=False,
        label='Nom',
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "style": "text-transform: uppercase",
            "onblur": "this.value=this.value.toUpperCase()"
        })
    )
    prenom = forms.CharField(
        required=False,
        label='Prénom',
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm",
            "style": "text-transform: capitalize",
            "onchange": "this.value=capitalize(this.value)"
        })
    )
    stagiaire = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input"
        })
    )
    diffusion = forms.ChoiceField(
        choices = (DIFFUSION_CHOIX),
        required=False,
        label='Diffusion',
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    date_debut = forms.DateField(
        label='Date de début du contrat',
        required=True,
        widget=forms.DateInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    date_fin = forms.DateField(
        label='Date de fin du contrat',
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control form-control-sm"
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
    agence_id = forms.ModelChoiceField(
        queryset=Agence.objects.all(),
        label='Agence',
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    isactif = forms.BooleanField(
        required=False,
        initial=True,
        label='En fonction',
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input"
        })
    )


class AgenceForm(forms.ModelForm):
    class Meta: 
        model = Agence
        fields = '__all__'

    nom_agence = forms.CharField(
        required=True,
        label="Nom de l'agence",
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class PersonnelNoteForm(forms.ModelForm):
    class Meta:
        model = PersonnelNote
        fields = '__all__'

    personnel_id = forms.IntegerField(
        required=False,
    )
    write_by_id = forms.IntegerField(
        required=False,
    )
    write_date = forms.DateTimeField(
        required=False,
    )
    note = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "cols": "30",
            "rows": "1",
        })
    )


class TypeCompteForm(forms.ModelForm):
    class Meta:
        model = TypeCompte
        fields = '__all__'

    nom_type = forms.CharField(
        label="Type de compte",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class CompteForm(forms.ModelForm):
    class Meta:
        model = Compte
        fields = '__all__'

    personnel_id = forms.ModelChoiceField(
        queryset=Personnel.objects.all().order_by('nom'),
        label="Nom",
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    type_compte_id = forms.ModelChoiceField(
        queryset=TypeCompte.objects.all().order_by('nom_type'),
        required=True,
        label="Type de compte",
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    login = forms.CharField(
        label="Identifiant",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    default_pwd = forms.CharField(
        label="Mot de passe (par défaut)",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    lien_site = forms.CharField(
        label="Lien vers le site",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    isactif = forms.BooleanField(
        required=False,
        initial=True,
        label='En fonction',
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input"
        })
    )


class RpmForm(forms.ModelForm):
    class Meta:
        model = Rpm
        fields = '__all__'

    # Liste des équipements ayant une relation avec une adresse Ip
    list_rpm = Rpm.objects.all().values_list('mail_id', flat=True)

    personnel_id = forms.ModelChoiceField(
        queryset=Personnel.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    mail_id = forms.ModelChoiceField(
        queryset=Mail.objects.exclude(pk__in=list_rpm),
        label="Email",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
