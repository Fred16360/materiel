
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models.functions import Now
from distutils.util import strtobool
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


from .models import Personnel, Agence, PersonnelNote, TypeCompte, Compte, Rpm
from equipement.models import Rpe, Ripe
from mail.models import Mail
from .forms import PersonnelForm, AgenceForm, PersonnelNoteForm, TypeCompteForm, CompteForm, RpmForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


class PersonnelList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Personnel
    paginate_by = 50
    template_name = 'personnel_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personnel_list'] = Personnel.objects.filter(isactif=True).order_by('nom')
        context['stagiaire_list'] = Personnel.objects.filter(stagiaire=True).order_by('nom')
        context['no_actif_list'] = Personnel.objects.filter(isactif=False).order_by('nom')
        return context


@login_required(login_url='/accounts/login/')
def PersonnelCreate(request):
    form = PersonnelForm()

    if request.method == "POST":
        form = PersonnelForm(request.POST or None)
        if form.is_valid():
            form.save()
            # On recherche le dernier enregistrement pour l'afficher
            last = Personnel.objects.last()
            return redirect('personnel_update', pk=last.id)

    return render(request, "personnel_create.html", {'form': form, 'create': 1})


@login_required(login_url='/accounts/login/')
def PersonnelUpdate(request, pk):
    list_personnelnote = PersonnelNote.objects.filter(personnel_id=pk)
    list_equipement = Rpe.objects.filter(personnel_id=pk)
    list_compte = Compte.objects.filter(personnel_id=pk)
    list_mail = Rpm.objects.filter(personnel_id=pk)
    mac_adresse = Rpe.objects.filter(personnel_id=pk).values_list('equipement_id_id', flat=True)
    ip_adresse = Ripe.objects.filter(pk__in=list_equipement.values_list('equipement_id_id', flat=True))
    #ip_adresse = Ripe.objects.filter(equipement_id=mac_adresse.equipement_id)

    try:
        personnel = Personnel.objects.get(pk=pk)
    except Personnel.DoesNotExist:
        return redirect('personnel_list')
    form = PersonnelForm(request.POST or None, instance=personnel)
    if form.is_valid():
        form.save()
        return redirect('personnel_list')

    return render(request, "personnel_update.html", {
        'form': form, 
        'list_personnelnote': list_personnelnote, 
        'personnel_id': pk, 
        'list_equipement': list_equipement,
        'list_compte': list_compte,
        'list_mail': list_mail,
        'create': 0,
        'ip_adresse': ip_adresse
        })


class PersonnelDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Personnel
    fields = '__all__'
    template_name = 'personnel_confirm_delete.html'

    success_url = reverse_lazy('personnel_list')

     
class AgenceList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Agence
    template_name = 'agence_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agence_list'] = Agence.objects.all().order_by('nom_agence')
        return context


@login_required(login_url='/accounts/login/')
def AgenceCreate(request):
    form = AgenceForm()

    if request.method == "POST":
        form = AgenceForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('agence_list')

    return render(request, "agence_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def AgenceUpdate(request, pk):
    try:
        agence = Agence.objects.get(pk=pk)
    except Agence.DoesNotExist:
        return redirect('agence_list')
    form = AgenceForm(request.POST or None, instance=agence)
    if form.is_valid():
        form.save()
        return redirect('agence_list')

    return render(request, "agence_form.html", {'form': form})


class AgenceDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Agence
    fields = '__all__'
    template_name = 'agence_confirm_delete.html'

    success_url = reverse_lazy('agence_list')


@login_required(login_url='/accounts/login/')
def LoadPersonnelNote(request):
    personnelnote_list = list(PersonnelNote.objects.all().values())
    data = dict()
    data['personnelnote_list'] = personnelnote_list

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def AjaxSaveNote(request, pk):
    form = PersonnelNoteForm(request.POST or None)
    personnel = get_object_or_404(Personnel, pk=pk)
    if form.is_valid():
        personnelnote = PersonnelNote(
            personnel_id = personnel,
            write_by_id = request.user,
            note = request.POST['note_personnel'],
        )
        personnelnote.save()

        query = PersonnelNote.objects.filter(personnel_id=pk)
        list = []
        for row in query:
            list.append({
                'write_by_id':row.write_by_id.name+' '+row.write_by_id.firstname,
                'write_date':row.write_date.strftime(' %d/%m/%Y %H:%M:%S'),
                'note':row.note,
                })
        data = dict()
        data['personnelnote_list'] = list

        return JsonResponse(data)


class TypeCompteList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = TypeCompte
    template_name = 'typecompte_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['typecompte_list'] = TypeCompte.objects.all().order_by('nom_type')
        return context


@login_required(login_url='/accounts/login/')
def TypeCompteCreate(request):
    form = TypeCompteForm()

    if request.method == "POST":
        form = TypeCompteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('typecompte_list')

    return render(request, "typecompte_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def TypeCompteUpdate(request, pk):
    try:
        typecompte = TypeCompte.objects.get(pk=pk)
    except TypeCompte.DoesNotExist:
        return redirect('typecompte_list')
    form = TypeCompteForm(request.POST or None, instance=typecompte)
    if form.is_valid():
        form.save()
        return redirect('typecompte_list')

    return render(request, "typecompte_form.html", {'form': form})


class TypeCompteDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = TypeCompte
    fields = '__all__'
    template_name = 'typecompte_confirm_delete.html'

    success_url = reverse_lazy('typecompte_list')


class CompteList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Compte
    template_name = 'compte_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compte_list'] = Compte.objects.all().order_by('personnel_id')
        return context


@login_required(login_url='/accounts/login/')
def CompteCreate(request):
    form = CompteForm()

    if request.method == "POST":
        form = CompteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('compte_list')

    return render(request, "compte_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def CompteUpdate(request, pk):
    try:
        compte = Compte.objects.get(pk=pk)
    except Compte.DoesNotExist:
        return redirect('compte_list')
    form = CompteForm(request.POST or None, instance=compte)
    if form.is_valid():
        form.save()
        return redirect('compte_list')

    return render(request, "compte_form.html", {'form': form})


class CompteDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Compte
    fields = '__all__'
    template_name = 'compte_confirm_delete.html'

    success_url = reverse_lazy('compte_list')


@login_required(login_url='/accounts/login/')
def CompteCreatePopup(request, pk):
    form = CompteForm()
    
    if request.method == "POST":
        form = CompteForm(request.POST or None)
        if form.is_valid():
            personnel = get_object_or_404(Personnel, pk=pk)
            type_compte = get_object_or_404(TypeCompte, pk=request.POST['type_compte_id'])
            compte = Compte(
                personnel_id = personnel,
                type_compte_id = type_compte,
                login = request.POST['login'],
                default_pwd = request.POST['default_pwd'],
                lien_site = request.POST['lien_site'],
                isactif = strtobool(request.POST['isactif']),
            )
            compte.save()        
            return redirect('personnel_update', pk=pk)

    return render(request, "compte_form_popup.html", {'form': form})


@login_required(login_url='/accounts/login/')
def CompteUpdatePopup(request, pk):
    try:
        compte_id = Compte.objects.get(pk=pk)
    except Compte.DoesNotExist:
        return redirect('personnel_update', pk=pk)

    form = CompteForm(request.POST or None, instance=compte_id)
    if form.is_valid():
        personnel = get_object_or_404(Personnel, pk=pk)
        type_compte = get_object_or_404(TypeCompte, pk=request.POST['type_compte_id'])
        compte = Compte(
            personnel_id = personnel,
            type_compte_id = type_compte,
            login = request.POST['login'],
            default_pwd = request.POST['default_pwd'],
            lien_site = request.POST['lien_site'],
            isactif = strtobool(request.POST['isactif']),
        )
        compte.save()  
        return redirect('personnel_update', pk=pk)

    return render(request, "compte_form_popup.html", {'form': form})


@login_required(login_url='/accounts/login/')
def RpmCreatePopup(request, pk):
    form = RpmForm()

    if request.method == "POST":
        form = RpmForm(request.POST or None)
        if form.is_valid():
            personnel = get_object_or_404(Personnel, pk=pk)
            mail = get_object_or_404(Mail, pk=request.POST['mail_id'])
            rpm = Rpm(
                personnel_id = personnel,
                mail_id = mail,
            )
            rpm.save()
            return redirect('personnel_update', pk=pk)
    
    return render(request, "rpm_popup_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def RpmDelete(request, pk):
    rpm = get_object_or_404(Rpm, pk=pk)
    if request.method == "POST":
        rpm.delete()
        HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, "rpm_confirm_delete.html", {'rpm': rpm})



