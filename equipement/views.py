from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from datetime import datetime
from django.utils.dateparse import parse_date
from django.http import JsonResponse
from distutils.util import strtobool
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ripe, TypeEquipement, Marque, Modele, Seller, Equipement, Rpe, EquipementNote
from personnel.models import Personnel
from .forms import TypeEquipementForm, MarqueForm, ModeleForm, SellerForm, EquipementForm, RpeForm, EquipementNoteForm, RipeForm

# Create your views here.
class TypeEquipementList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = TypeEquipement

    template_name = 'typeequipement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['typeequipement_list'] = TypeEquipement.objects.all().order_by('nom_type')
        return context


@login_required(login_url='/accounts/login/')
def TypeEquipementCreate(request):
    form = TypeEquipementForm()

    if request.method == "POST":
        form = TypeEquipementForm(request.POST or None)
        if form.is_valid():
            form.save()
            
    return render(request, "typeequipement_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def TypeEquipementUpdate(request, pk):
    try:
        type = TypeEquipement.objects.get(pk=pk)
    except TypeEquipement.DoesNotExist:
        return redirect('societe_list')
    form = TypeEquipementForm(request.POST or None, instance=type)
    if form.is_valid():
        form.save()

    return render(request, "typeequipement_form.html", {'form': form})


class TypeEquipementDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = TypeEquipement
    fields = '__all__'
    template_name = 'typeequipement_confirm_delete.html'

    success_url = reverse_lazy('typeequipement_list')


class MarqueList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Marque

    template_name = 'marque_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marque_list'] = Marque.objects.all().order_by('nom_marque')
        return context


@login_required(login_url='/accounts/login/')
def MarqueCreate(request):
    form = MarqueForm()

    if request.method == "POST":
        form = MarqueForm(request.POST or None)
        if form.is_valid():
            form.save()
            
    return render(request, "marque_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def MarqueUpdate(request, pk):
    try:
        marque = Marque.objects.get(pk=pk)
    except Marque.DoesNotExist:
        return redirect('marque_list')
    form = MarqueForm(request.POST or None, instance=marque)
    if form.is_valid():
        form.save()

    return render(request, "marque_form.html", {'form': form})


class MarqueDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Marque
    fields = '__all__'
    template_name = 'marque_confirm_delete.html'

    success_url = reverse_lazy('marque_list')


class ModeleList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Modele

    template_name = 'modele_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modele_list'] = Modele.objects.all().order_by('nom_modele')
        return context


@login_required(login_url='/accounts/login/')
def ModeleCreate(request):
    form = ModeleForm()

    if request.method == "POST":
        form = ModeleForm(request.POST or None)
        if form.is_valid():
            form.save()
            
    return render(request, "modele_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def ModeleUpdate(request, pk):
    try:
        marque = Modele.objects.get(pk=pk)
    except Modele.DoesNotExist:
        return redirect('modele_list')
    form = ModeleForm(request.POST or None, instance=marque)
    if form.is_valid():
        form.save()

    return render(request, "modele_form.html", {'form': form})


class ModeleDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Modele
    fields = '__all__'
    template_name = 'modele_confirm_delete.html'

    success_url = reverse_lazy('modele_list')


class SellerList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Seller

    template_name = 'seller_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seller_list'] = Seller.objects.all().order_by('seller_name')
        return context


@login_required(login_url='/accounts/login/')
def SellerCreate(request):
    form = SellerForm()

    if request.method == "POST":
        form = SellerForm(request.POST or None)
        if form.is_valid():
            form.save()
            
    return render(request, "seller_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def SellerUpdate(request, pk):
    try:
        seller = Seller.objects.get(pk=pk)
    except Seller.DoesNotExist:
        return redirect('seller_list')
    form = SellerForm(request.POST or None, instance=seller)
    if form.is_valid():
        form.save()

    return render(request, "seller_form.html", {'form': form})


class SellerDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Seller
    fields = '__all__'
    template_name = 'seller_confirm_delete.html'

    success_url = reverse_lazy('seller_list')


class EquipementList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Equipement
    template_name = 'equipement_list.html'

    def get_context_data(self, **kwargs):
        list_rpe = Rpe.objects.all().values_list('equipement_id', flat=True)
        
        context = super().get_context_data(**kwargs)
        context['equipement_list'] = Equipement.objects.all().order_by('sig_id')
        context['equipement_libre_list'] = Equipement.objects.exclude(pk__in=list_rpe).order_by('sig_id')
        return context


@login_required(login_url='/accounts/login/')
def EquipementCreate(request):
    form = EquipementForm()

    if request.method == "POST":
        form = EquipementForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('equipement_list')

    return render(request, "equipement_form.html", {'form': form, 'create': 1})


@login_required(login_url='/accounts/login/')
def EquipementUpdate(request, pk):
    list_equipementnote = EquipementNote.objects.filter(equipement_id=pk)
    list_personnel = Rpe.objects.filter(equipement_id=pk)

    try:
        equipement = Equipement.objects.get(pk=pk)
    except Equipement.DoesNotExist:
        return redirect('equipement_list')
    form = EquipementForm(request.POST or None, instance=equipement)
    if form.is_valid():
        form.save()
        return redirect('equipement_list')
        
    return render(request, "equipement_form.html", {
        'form': form, 
        'create': 0, 
        'list_equipementnote': list_equipementnote,
        'list_personnel': list_personnel,
        'equipement_id': pk
        })


@login_required(login_url='/accounts/login/')
def EquipementPopupUpdate(request, pk):
    try:
        equipement = Equipement.objects.get(pk=pk)
    except Equipement.DoesNotExist:
        return redirect('equipement_list')
    form = EquipementForm(request.POST or None, instance=equipement)
    if form.is_valid():
        form.save()
                
    return render(request, "equipement_popup_form.html", {'form': form})


class EquipementDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Equipement
    fields = '__all__'
    template_name = 'equipement_confirm_delete.html'

    success_url = reverse_lazy('equipement_list')


@login_required(login_url='/accounts/login/')
def RpeCreate(request, pk):
    form = RpeForm()

    if request.method == "POST":
        form = RpeForm(request.POST or None)
        if form.is_valid():
            personnel = get_object_or_404(Personnel, pk=pk)
            equipement = get_object_or_404(Equipement, pk=request.POST['equipement_id'])
            rpe = Rpe(
                personnel_id = personnel,
                equipement_id = equipement,
                date_debut = parse_date(request.POST['date_debut']),
                date_fin = parse_date(request.POST['date_fin']),
            )
            rpe.save()
            return redirect('personnel_update', pk=pk)
            
    return render(request, "rpe_popup_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def RpeDelete(request, pk):
    rpe = get_object_or_404(Rpe, pk=pk)
    if request.method == "POST":
        rpe.delete()
        HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, "rpe_confirm_delete.html", {'rpe': rpe})


@login_required(login_url='/accounts/login/')
def LoadTypeEquipement(request):
    typeequipement_list = list(TypeEquipement.objects.all().values())
    data = dict()
    data['typeequipement_list'] = typeequipement_list

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def LoadMarque(request):
    marque_list = list(Marque.objects.all().values())
    data = dict()
    data['marque_list'] = marque_list

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def LoadModele(request):
    modele_list = list(Modele.objects.all().values())
    data = dict()
    data['modele_list'] = modele_list

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def AjaxSaveNoteEquipement(request, pk):
    form = EquipementNoteForm(request.POST or None)
    equipement = get_object_or_404(Equipement, pk=pk)
    if form.is_valid():
        equipementnote = EquipementNote(
            equipement_id = equipement,
            write_by_id = request.user,
            note = request.POST['note_equipement'],
        )
        equipementnote.save()

        query = EquipementNote.objects.filter(equipement_id=pk)
        list = []
        for row in query:
            list.append({
                'write_by_id':row.write_by_id.name+' '+row.write_by_id.firstname,
                'write_date':row.write_date.strftime(' %d/%m/%Y %H:%M:%S'),
                'note':row.note,
                })
        data = dict()
        data['equipementnote_list'] = list

        return JsonResponse(data)


class RipeList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Ripe
    template_name = 'ripe_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ripe_list'] = Ripe.objects.all().order_by('ip_machine')
        return context


@login_required(login_url='/accounts/login/')
def RipeCreate(request):
    # LISTE DES EQUIPEMENTS AVEC MAC ADRESSE
    list_mac = Equipement.objects.exclude(Q(mac_addr1="") & Q(mac_addr2=""))
    # LISTE DES EQUIPEMENTS AVEC UNE ADRESSE IP
    query = Ripe.objects.exclude(equipement_id=None).values_list('equipement_id', flat=True)
    list_ip = list_mac.exclude(id__in=query)
    # LISTE DES EQUIPEMENTS AVEC UNE ADRESSE MAC, SANS ADRESSE IP + EQUIPEMENT EN MODIFICATION
    list_equipement = list_ip.order_by('sig_id')

    form = RipeForm()
    if request.method == "POST":
        form = RipeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('ripe_list')

    return render(request, "ripe_form.html", {
        'form': form, 
        'base_template': "popup.html",
        'list_equipement': list_equipement
        })


@login_required(login_url='/accounts/login/')
def RipeUpdate(request, pk):
    try:
        ripe = Ripe.objects.get(pk=pk)
    except Ripe.DoesNotExist:
        return redirect('ripe_list')
   
    # LISTE DES EQUIPEMENTS AVEC MAC ADRESSE
    list_mac = Equipement.objects.exclude(Q(mac_addr1="") & Q(mac_addr2=""))
    # LISTE DES EQUIPEMENTS AVEC UNE ADRESSE IP
    query = Ripe.objects.exclude(equipement_id=None).values_list('equipement_id', flat=True)
    list_ip = list_mac.exclude(id__in=query)
    # EQUIPEMENT EN MODIFICATION
    query = Ripe.objects.filter(id=pk).values_list('equipement_id', flat=True)
    equipement_update = Equipement.objects.filter(id__in=query)
    if equipement_update:
        id_update = equipement_update[0].id
    else:
        id_update = 0
    # LISTE DES EQUIPEMENTS AVEC UNE ADRESSE MAC, SANS ADRESSE IP + EQUIPEMENT EN MODIFICATION
    list_equipement = list_ip.union(equipement_update).order_by('sig_id')
    
    form = RipeForm(request.POST or None, instance=ripe)
    if form.is_valid():
        form.save()
        return redirect('ripe_list')
        
    return render(request, "ripe_form.html", {
        'form': form, 
        'base_template': "popup.html",
        'id_update': id_update,
        'equipement_update': equipement_update,
        'list_equipement': list_equipement
        })


@login_required(login_url='/accounts/login/')
def RipeDelete(request, pk):
    ripe = get_object_or_404(Ripe, pk=pk)
    if request.method == "POST":
        ripe.delete()
        HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, "ripe_confirm_delete.html", {'ripe': ripe})


