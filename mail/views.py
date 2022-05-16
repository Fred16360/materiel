from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mail, ConfigMail, HebergeurMail
from .forms import MailForm, ConfigMailForm, HebergeurMailForm

# Create your views here.

class MailList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Mail

    template_name = 'mail_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mail_list'] = Mail.objects.all()
        return context


@login_required(login_url='/accounts/login/')
def MailCreate(request):
    form = MailForm()

    if request.method == "POST":
        form = MailForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mail_list')

    return render(request, "mail_create.html", {'form': form})


@login_required(login_url='/accounts/login/')
def MailCreatePopup(request):
    form = MailForm()

    if request.method == "POST":
        form = MailForm(request.POST or None)
        if form.is_valid():
            form.save()

    return render(request, "mail_create_popup.html", {'form': form})


@login_required(login_url='/accounts/login/')
def MailUpdate(request, pk):
    try:
        mail = Mail.objects.get(pk=pk)
    except Mail.DoesNotExist:
        return redirect('mail_list')
    form = MailForm(request.POST or None, instance=mail)
    if form.is_valid():
        form.save()
        return redirect('mail_list')

    return render(request, "mail_create.html", {'form': form})


class MailDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Mail
    fields = '__all__'
    template_name = 'mail_confirm_delete.html'

    success_url = reverse_lazy('mail_list')


@login_required(login_url='/accounts/login/')
def LoadMail(request):
    mail_list = list(Mail.objects.all().values())
    data = dict()
    data['mail_list'] = mail_list

    return JsonResponse(data)


class ConfigMailList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = ConfigMail

    template_name = 'configmail_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['configmail_list'] = ConfigMail.objects.all()
        return context


@login_required(login_url='/accounts/login/')
def ConfigMailCreate(request):
    form = ConfigMailForm()

    if request.method == "POST":
        form = ConfigMailForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('configmail_list')

    return render(request, "configmail_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def ConfigMailUpdate(request, pk):
    try:
        configmail = ConfigMail.objects.get(pk=pk)
    except ConfigMail.DoesNotExist:
        return redirect('configmail_list')
    form = ConfigMailForm(request.POST or None, instance=configmail)
    if form.is_valid():
        form.save()
        return redirect('configmail_list')

    return render(request, "configmail_form.html", {'form': form})


class ConfigMailDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = ConfigMail
    fields = '__all__'
    template_name = 'configmail_confirm_delete.html'

    success_url = reverse_lazy('configmail_list')


class HebergeurList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = HebergeurMail

    template_name = 'hebergeurmail_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hebergeurmail_list'] = HebergeurMail.objects.all()
        return context


@login_required(login_url='/accounts/login/')
def HebergeurMailCreate(request):
    form = HebergeurMailForm()

    if request.method == "POST":
        form = HebergeurMailForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('hebergeurmail_list')

    return render(request, "hebergeurmail_form.html", {'form': form})


@login_required(login_url='/accounts/login/')
def HebergeurMailUpdate(request, pk):
    try:
        mail = HebergeurMail.objects.get(pk=pk)
    except Mail.DoesNotExist:
        return redirect('hebergeurmail_list')
    form = HebergeurMailForm(request.POST or None, instance=mail)
    if form.is_valid():
        form.save()
        return redirect('hebergeurmail_list')

    return render(request, "hebergeurmail_form.html", {'form': form})


class HebergeurMailDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = HebergeurMail
    fields = '__all__'
    template_name = 'hebergeurmail_confirm_delete.html'

    success_url = reverse_lazy('hebergeurmail_list')
