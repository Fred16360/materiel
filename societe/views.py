from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SocieteForm
from .models import Societe
# Create your views here.


class SocieteList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Societe
    template_name = 'societe_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['societe_list'] = Societe.objects.all()
        return context


@login_required(login_url='/accounts/login/')
def SocieteCreate(request):
    form = SocieteForm()

    if request.method == "POST":
        form = SocieteForm(request.POST or None)
        if form.is_valid():
            form.save()
            
    return render(request, "societe_create.html", {'form': form})


@login_required(login_url='/accounts/login/')
def SocieteCreatePopup(request):
    form = SocieteForm()

    if request.method == "POST":
        form = SocieteForm(request.POST or None)
        if form.is_valid():
            form.save()

    return render(request, "societe_create_popup.html", {'form': form})


@login_required(login_url='/accounts/login/')
def SocieteUpdate(request, pk):
    try:
        societe = Societe.objects.get(pk=pk)
    except Societe.DoesNotExist:
        return redirect('societe_list')
    form = SocieteForm(request.POST or None, instance=societe)
    if form.is_valid():
        form.save()

    return render(request, "societe_create.html", {'form': form})


class SocieteDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Societe
    fields = '__all__'
    template_name = 'societe_confirm_delete.html'

    success_url = reverse_lazy('societe_list')


@login_required(login_url='/accounts/login/')
def LoadSociete(request):
    societe_list = list(Societe.objects.all().values())
    data = dict()
    data['societe_list'] = societe_list

    return JsonResponse(data)