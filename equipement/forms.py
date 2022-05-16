from django.forms import ModelForm
from django import forms
from django.forms.models import ModelChoiceField
from . import models
from django.db.models import Q

from .models import Equipement, Modele, Ripe, Rpe, TypeEquipement, Marque, Modele, Seller, EquipementNote 
from personnel.models import Personnel


class TypeEquipementForm(forms.ModelForm):
    class Meta:
        model = TypeEquipement
        fields = '__all__'

    nom_type = forms.CharField(
        label="Type d'équipement",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class MarqueForm(forms.ModelForm):
    class Meta :
        model = Marque
        fields = '__all__'

    nom_marque = forms.CharField(
        label="Nom de la marque",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class ModeleForm(forms.ModelForm):
    class Meta :
        model = Modele
        fields = '__all__'

    nom_modele = forms.CharField(
        label="Nom du modèle",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class SellerForm(forms.ModelForm):
    class Meta :
        model = Seller
        fields = '__all__'

    seller_name = forms.CharField(
        label="Nom du vendeur",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    phone_number = forms.CharField(
        label="N° Téléphone",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class EquipementForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = '__all__'

    sig_id = forms.CharField(
        label="Référence SIG",
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    type_id = forms.ModelChoiceField(
        queryset=TypeEquipement.objects.all().order_by('nom_type'),
        label="Type Equipement",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    marque = forms.ModelChoiceField(
        queryset=Marque.objects.all().order_by('nom_marque'),
        label="Marque",
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    modele = forms.ModelChoiceField(
        queryset=Modele.objects.all().order_by('nom_modele'),
        label="Modèle",
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    num_serie = forms.CharField(
        label="Numéro de série",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    detail = forms.CharField(
        label="Détail",
        required=False,
        widget=forms.Textarea(attrs={
            "cols": "30",
            "rows": "5",
        })
    )
    seller_id = forms.ModelChoiceField(
        queryset=Seller.objects.all().order_by('seller_name'),
        label="Vendeur",
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    buy_date = forms.DateField(
        label="Date d'achat",
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    guarantee_end_date = forms.DateField(
        label="Date de fin de garantie",
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    mac_addr1 = forms.CharField(
        label="Mac Adresse N°1",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    mac_addr2 = forms.CharField(
        label="Mac Adresse N°2",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class EquipementNoteForm(forms.ModelForm):
    class Meta:
        model = EquipementNote
        fields = '__all__'

    equipement_id = forms.IntegerField(
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
            "rows": "5",
        })
    )


class RpeForm(forms.ModelForm):
    class Meta:
        model = Rpe
        fields = '__all__'

    # Liste des équipements ayant une relation avec du personnel
    list_rpe = Rpe.objects.all().values_list('equipement_id', flat=True)

    personnel_id = forms.ModelChoiceField(
        queryset=Personnel.objects.all(),
        label="Nom personnel",
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    equipement_id = forms.ModelChoiceField(
        queryset=Equipement.objects.exclude(pk__in=list_rpe),
        label="Nom équipement",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )
    date_debut = forms.DateField(
        label="Date de début",
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    date_fin = forms.DateField(
        label="Date de fin",
        required=False,
        widget=forms.DateInput(attrs={
            "class": "form-control form-control-sm"
        })
    )


class RipeForm(forms.ModelForm):
    class Meta:
        model = Ripe
        fields = '__all__'

    # Liste des équipements ayant une relation avec une adresse Ip
    #list_ripe = Ripe.objects.all().exclude(equipement_id=None)

    ip_machine = forms.CharField(
        label='Adresse Ip',
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )
    description = forms.CharField(
        label="Description",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-sm"
        })
    )    
    equipement_id = forms.ModelChoiceField(
        queryset=Equipement.objects.all(),
        #queryset=Equipement.objects.exclude(pk__in=list_ripe),
        #initial={'equipement_id': instance},
        label="Nom équipement",
        required=False,
        widget=forms.Select(attrs={
            "class": "form-select form-select-sm"
        })
    )