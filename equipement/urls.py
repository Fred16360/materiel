from django.urls import path
from . import views

from .views import TypeEquipementList, TypeEquipementCreate, TypeEquipementUpdate, TypeEquipementDelete
from .views import MarqueList, MarqueCreate, MarqueUpdate, MarqueDelete
from .views import ModeleList, ModeleCreate, ModeleUpdate, ModeleDelete
from .views import SellerList, SellerCreate, SellerUpdate, SellerDelete
from .views import EquipementList, EquipementCreate, EquipementUpdate, EquipementDelete
from .views import LoadTypeEquipement
from .views import RpeCreate, AjaxSaveNoteEquipement
from .views import RipeList, RipeCreate, RipeUpdate, RipeDelete

urlpatterns = [

    path('type/list', TypeEquipementList.as_view(), name='typeequipement_list'),
    path('type/create', views.TypeEquipementCreate, name='typeequipement_create'),
    path('type/update/<int:pk>', views.TypeEquipementUpdate, name='typeequipement_update'),
    path('type/delete/<int:pk>', TypeEquipementDelete.as_view(), name='typeequipement_delete'),

    path('marque/list', MarqueList.as_view(), name='marque_list'),
    path('marque/create', views.MarqueCreate, name='marque_create'),
    path('marque/update/<int:pk>', views.MarqueUpdate, name='marque_update'),
    path('marque/delete/<int:pk>', MarqueDelete.as_view(), name='marque_delete'),

    path('modele/list', ModeleList.as_view(), name='modele_list'),
    path('modele/create', views.ModeleCreate, name='modele_create'),
    path('modele/update/<int:pk>', views.ModeleUpdate, name='modele_update'),
    path('modele/delete/<int:pk>', ModeleDelete.as_view(), name='modele_delete'),

    path('seller/list', SellerList.as_view(), name='seller_list'),
    path('seller/create', views.SellerCreate, name='seller_create'),
    path('seller/update/<int:pk>', views.SellerUpdate, name='seller_update'),
    path('seller/delete/<int:pk>', SellerDelete.as_view(), name='seller_delete'),

    path('list', EquipementList.as_view(), name='equipement_list'),
    path('create', views.EquipementCreate, name='equipement_create'),
    path('update/<int:pk>', views.EquipementUpdate, name='equipement_update'),
    path('delete/<int:pk>', EquipementDelete.as_view(), name='equipement_delete'),

    path('rpe/create/<int:pk>', views.RpeCreate, name='rpe_create'),
    path('rpe/delete/<int:pk>', views.RpeDelete, name='rpe_delete'),

    path('ripe/list', RipeList.as_view(), name='ripe_list'),
    path('ripe/create', views.RipeCreate, name='ripe_create'),
    path('ripe/update/<int:pk>', views.RipeUpdate, name='ripe_update'),
    path('ripe/delete/<int:pk>', views.RipeDelete, name='ripe_delete'),

    # REQUETES AJAX
    path('load/equipement', views.LoadTypeEquipement, name='typeequipement_load'),
    path('load/marque', views.LoadMarque, name='marque_load'),
    path('load/modele', views.LoadModele, name='modele_load'),

    path('note/<int:pk>', views.AjaxSaveNoteEquipement, name='save_note_equipement'),
]