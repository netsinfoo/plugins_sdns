from django.urls import path
from extras.views import ObjectChangeLogView, ObjectJournalView
from . import views
from sdns.models import *


app_name = 'sdns'



urlpatterns = [
   path('', views.RegisterView.as_view(), name='sdns') ,
   # ====================Registros======================================
   path('register/', views.RegisterListView.as_view(), name='register_list') ,
   path("register/add/", views.RegisterEditView.as_view(), name='register_add'),
   path('register/import/', views.RegisterBulkImportView.as_view(), name='register_import'),
  # path('register/edit/', views.RegisterBulkEditView.as_view(), name='register_bulk_edit'),
   path("register/delete/", views.RegisterBulkDeleteView.as_view(), name='register_bulk_delete'),
   path('register/<int:pk>/', views.RegisterView.as_view(), name='register'),
   path('register/<int:pk>/edit/', views.RegisterEditView.as_view(), name='register_edit'),
   path('register/<int:pk>/delete/', views.RegisterDeleteView.as_view(), name='register_delete'),
   path('register/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='register_changelog', kwargs={'model': Register}),
   path('register/<int:pk>/journal/', ObjectJournalView.as_view(), name='register_journal', kwargs={'model': Register}),
   # ========================= DOMAIN ==============
   path('domain/', views.DomainListView.as_view(), name='domain_list') ,
   path("domain/add/", views.DomainCreateView.as_view(), name='domain_add'),
   path('domain/import/', views.DomainBulkImportView.as_view(), name='domain_import'),
   #path('domain/edit/', views.DomainBulkEditView.as_view(), name='domain_bulk_edit'),
   path("domain/delete/", views.DomainBulkDeleteView.as_view(), name='domain_bulk_delete'),
   path('domain/<int:pk>/', views.DomainView.as_view(), name='domain'),
   path('domain/<int:pk>/edit/', views.DomainEditView.as_view(), name='domain_edit'),
   path('domain/<int:pk>/delete/', views.DomainDeleteView.as_view(), name='domain_delete'),
   # ========================= RESP ==============
   path('resp/', views.RespListView.as_view(), name='resp_list'),
   path("resp/add/", views.RespCreateView.as_view(), name='resp_add'),
   path('resp/import/', views.RespBulkImportView.as_view(), name='resp_import'),
   #path('resp/edit/', views.RespBulkEditView.as_view(), name='resp_bulk_edit'),
   path("resp/delete/", views.RespBulkDeleteView.as_view(), name='resp_bulk_delete'),
   path('resp/<int:pk>/', views.RespView.as_view(), name='resp'),
   path('resp/<int:pk>/edit/', views.RespEditView.as_view(), name='resp_edit'),
   path('resp/<int:pk>/delete/', views.RespDeleteView.as_view(), name='resp_delete'),
   # ========================= Ns ==============
   path('ns/', views.NsListView.as_view(), name='ns_list') ,
   path("ns/add/", views.NsCreateView.as_view(), name='ns_add'),
   path('ns/import/', views.NsBulkImportView.as_view(), name='ns_import'),
   #path('ns/edit/', views.NsBulkEditView.as_view(), name='ns_bulk_edit'),
   path("ns/delete/", views.NsBulkDeleteView.as_view(), name='ns_bulk_delete'),
   path('ns/<int:pk>/', views.NsView.as_view(), name='ns'),
   path('ns/<int:pk>/edit/', views.NsEditView.as_view(), name='ns_edit'),
   path('ns/<int:pk>/delete/', views.NsDeleteView.as_view(), name='ns_delete'),
   # ========================= Mx ==============
   path('mx', views.MxListView.as_view(), name='mx_list') ,
   path("mx/add/", views.MxCreateView.as_view(), name='mx_add'),
   path('mx/import/', views.MxBulkImportView.as_view(), name='mx_import'),
   #path('mx/edit/', views.MxBulkEditView.as_view(), name='mx_bulk_edit'),
   path("mx/delete/", views.MxBulkDeleteView.as_view(), name='mx_bulk_delete'),
   path('mx/<int:pk>/', views.MxView.as_view(), name='mx'),
   path('mx/<int:pk>/edit/', views.MxEditView.as_view(), name='mx_edit'),
   path('mx/<int:pk>/delete/', views.MxDeleteView.as_view(), name='mx_delete'),
   # ========================= Cts ==============
   path('cts', views.CtsListView.as_view(), name='cts_list') ,
   path("cts/add/", views.CtsCreateView.as_view(), name='cts_add'),
   path('cts/import/', views.CtsBulkImportView.as_view(), name='cts_import'),
   #path('cts/edit/', views.CtsBulkEditView.as_view(), name='cts_bulk_edit'),
   path("cts/delete/", views.CtsBulkDeleteView.as_view(), name='cts_bulk_delete'),
   path('cts/<int:pk>/', views.CtsView.as_view(), name='cts'),
   path('cts/<int:pk>/edit/', views.CtsEditView.as_view(), name='cts_edit'),
   path('cts/<int:pk>/delete/', views.CtsDeleteView.as_view(), name='cts_delete'),
   # ========================= DomainServ ==============
   path('domainserv', views.DomainServListView.as_view(), name='domainserv_list') ,
   path("domainserv/add/", views.DomainServCreateView.as_view(), name='domainserv_add'),
   path('domainserv/import/', views.DomainServBulkImportView.as_view(), name='domainserv_import'),
   #path('domainserv/edit/', views.DomainServBulkEditView.as_view(), name='domainserv_bulk_edit'),
   path("domainserv/delete/", views.DomainServBulkDeleteView.as_view(), name='domainserv_bulk_delete'),
   path('domainserv/<int:pk>/', views.DomainServView.as_view(), name='domainserv'),
   path('domainserv/<int:pk>/edit/', views.DomainServEditView.as_view(), name='domainserv_edit'),
   path('domainserv/<int:pk>/delete/', views.DomainServDeleteView.as_view(), name='domainserv_delete'),
]
