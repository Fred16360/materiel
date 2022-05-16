from django.forms import ModelForm
from django import forms

from .models import Societe


class SocieteForm(forms.ModelForm):
    class Meta:
        model = Societe
        fields = '__all__'

    nom_societe = forms.CharField(
        label='Nom',
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    siret = forms.CharField(
        label='SIRET',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    ape = forms.CharField(
        label='APE',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    nom_gerant = forms.CharField(
        label='Nom du gérant',
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )