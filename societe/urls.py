from django.urls import path

from . import views
from .views import SocieteCreate, SocieteList, SocieteUpdate, SocieteDelete, SocieteCreatePopup

urlpatterns = [

    path('create', views.SocieteCreate, name='societe_create'),
    path('create-popup', views.SocieteCreatePopup, name='societe_create_popup'),
    path('list', SocieteList.as_view(), name='societe_list'),
    path('update/<int:pk>', views.SocieteUpdate, name='societe_update'),
    path('delete/<int:pk>', SocieteDelete.as_view(), name='societe_delete'),

    path('ajax', views.LoadSociete, name='ajax_load_societe'),   # Ajax

]