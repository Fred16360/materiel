from django.urls import path

from . import views
from .views import MailList, MailCreate, MailCreatePopup, LoadMail, MailUpdate, MailDelete
from .views import ConfigMailList, ConfigMailUpdate, ConfigMailDelete
from .views import HebergeurList, HebergeurMailUpdate, HebergeurMailDelete

urlpatterns = [

    path('list', MailList.as_view(), name='mail_list'),
    path('create', views.MailCreate, name='mail_create'),
    path('create-popup', views.MailCreatePopup, name='mail_create_popup'),
    path('update/<int:pk>', views.MailUpdate, name='mail_update'),
    path('delete/<int:pk>', MailDelete.as_view(), name='mail_delete'),

    path('ajax', views.LoadMail, name='ajax_load_mail'),

    path('config/list', ConfigMailList.as_view(), name='configmail_list'),
    path('config/create', views.ConfigMailCreate, name='configmail_create'),
    path('config/update/<int:pk>', views.ConfigMailUpdate, name='configmail_update'),
    path('config/delete/<int:pk>', ConfigMailDelete.as_view(), name='configmail_delete'),

    path('hebergeur/list', HebergeurList.as_view(), name='hebergeurmail_list'),
    path('hebergeur/create', views.HebergeurMailCreate, name='hebergeurmail_create'),
    path('hebergeur/update/<int:pk>', views.HebergeurMailUpdate, name='hebergeurmail_update'),
    path('hebergeur/delete/<int:pk>', HebergeurMailDelete.as_view(), name='hebergeurmail_delete'),
    
]

