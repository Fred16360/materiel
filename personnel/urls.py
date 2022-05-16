from django.urls import path

from . import views

from .views import PersonnelList, PersonnelCreate, PersonnelUpdate, PersonnelDelete, AjaxSaveNote, RpmDelete
from .views import AgenceList, AgenceCreate, AgenceUpdate, AgenceDelete
from .views import TypeCompteList, TypeCompteCreate, TypeCompteUpdate, TypeCompteDelete
from .views import CompteList, CompteCreate, CompteUpdate, CompteDelete
from .views import CompteCreatePopup, RpmCreatePopup, RpmDelete

urlpatterns = [
    path('index', views.index, name='index'),
    path('list', PersonnelList.as_view(), name='personnel_list'),
    path('create', views.PersonnelCreate, name='personnel_create'),
    path('update/<int:pk>', views.PersonnelUpdate, name='personnel_update'),
    path('delete/<int:pk>', PersonnelDelete.as_view(), name='personnel_delete'),

    path('agence/list', AgenceList.as_view(), name='agence_list'),
    path('agence/create', views.AgenceCreate, name='agence_create'),
    path('agence/update/<int:pk>', views.AgenceUpdate, name='agence_update'),
    path('agence/delete/<int:pk>', AgenceDelete.as_view(), name='agence_delete'),

    path('note/<int:pk>', views.AjaxSaveNote, name='save_note'),

    path('typecompte/list', TypeCompteList.as_view(), name='typecompte_list'),
    path('typecompte/create', views.TypeCompteCreate, name='typecompte_create'),
    path('typecompte/update/<int:pk>', views.TypeCompteUpdate, name='typecompte_update'),
    path('typecompte/delete/<int:pk>', TypeCompteDelete.as_view(), name='typecompte_delete'),

    path('compte/list', CompteList.as_view(), name='compte_list'),
    path('compte/create', views.CompteCreate, name='compte_create'),
    path('compte/update/<int:pk>', views.CompteUpdate, name='compte_update'),
    path('compte/delete/<int:pk>', CompteDelete.as_view(), name='compte_delete'),

    path('compte/popup/create/<int:pk>', views.CompteCreatePopup, name='compte_create_popup'),
    path('compte/popup/update/<int:pk>', views.CompteUpdatePopup, name='compte_update_popup'),

    path('rpm/popup/create/<int:pk>', views.RpmCreatePopup, name='rpm_create_popup'),
    path('rpm/delete/<int:pk>', views.RpmDelete, name='rpm_delete'),
]

