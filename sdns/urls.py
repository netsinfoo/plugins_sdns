from django.urls import path
from . import views

urlpatterns = [
   # ====================Registros======================================
   path('register', views.RegisterListView.as_view(), name='register_list') ,
   path("register/add/", views.RegisterCreateView.as_view(), name='register_add'),
   path("register/delete/", views.RegisterBulkDeleteView.as_view(), name='register_bulk_delete'),
   path('register/<int:pk>/', views.RegisterView.as_view(), name='register'),
   path('register/<int:pk>/edit/', views.RegisterEditView.as_view(), name='register_edit'),
   path('register/<int:pk>/delete/', views.RegisterDeleteView.as_view(), name='register_delete'),
   # ========================= DOMAIN ==============
   path('domain', views.DomainListView.as_view(), name='domain_list') ,
   path("domain/add/", views.DomainCreateView.as_view(), name='domain_add'),
   path("domain/delete/", views.DomainBulkDeleteView.as_view(), name='domain_bulk_delete'),
   path('domain/<int:pk>/', views.DomainView.as_view(), name='domain'),
   path('domain/<int:pk>/edit/', views.DomainEditView.as_view(), name='domain_edit'),
   path('domain/<int:pk>/delete/', views.DomainDeleteView.as_view(), name='domain_delete'),
   # ========================= RESP ==============
   path('resp', views.RespListView.as_view(), name='resp_list') ,
   path("resp/add/", views.RespCreateView.as_view(), name='resp_add'),
   path("resp/delete/", views.RespBulkDeleteView.as_view(), name='resp_bulk_delete'),
   path('resp/<int:pk>/', views.RespView.as_view(), name='resp'),
   path('resp/<int:pk>/edit/', views.RespEditView.as_view(), name='resp_edit'),
   path('resp/<int:pk>/delete/', views.RespDeleteView.as_view(), name='resp_delete'),
   # ========================= Ns ==============
   path('ns', views.NsListView.as_view(), name='ns_list') ,
   path("ns/add/", views.NsCreateView.as_view(), name='ns_add'),
   path("ns/delete/", views.NsBulkDeleteView.as_view(), name='ns_bulk_delete'),
   path('ns/<int:pk>/', views.NsView.as_view(), name='ns'),
   path('ns/<int:pk>/edit/', views.NsEditView.as_view(), name='ns_edit'),
   path('ns/<int:pk>/delete/', views.NsDeleteView.as_view(), name='ns_delete'),
   # ========================= Mx ==============
   path('mx', views.MxListView.as_view(), name='mx_list') ,
   path("mx/add/", views.MxCreateView.as_view(), name='mx_add'),
   path("mx/delete/", views.MxBulkDeleteView.as_view(), name='mx_bulk_delete'),
   path('mx/<int:pk>/', views.MxView.as_view(), name='mx'),
   path('mx/<int:pk>/edit/', views.MxEditView.as_view(), name='mx_edit'),
   path('mx/<int:pk>/delete/', views.MxDeleteView.as_view(), name='mx_delete'),
   # ========================= Cts ==============
   path('cts', views.CtsListView.as_view(), name='cts_list') ,
   path("cts/add/", views.CtsCreateView.as_view(), name='cts_add'),
   path("cts/delete/", views.CtsBulkDeleteView.as_view(), name='cts_bulk_delete'),
   path('cts/<int:pk>/', views.CtsView.as_view(), name='cts'),
   path('cts/<int:pk>/edit/', views.CtsEditView.as_view(), name='cts_edit'),
   path('cts/<int:pk>/delete/', views.CtsDeleteView.as_view(), name='cts_delete'),
   # ========================= DomainServ ==============
   path('domainserv', views.DomainServListView.as_view(), name='domainserv_list') ,
   path("domainserv/add/", views.DomainServCreateView.as_view(), name='domainserv_add'),
   path("domainserv/delete/", views.DomainServBulkDeleteView.as_view(), name='domainserv_bulk_delete'),
   path('domainserv/<int:pk>/', views.DomainServView.as_view(), name='domainserv'),
   path('domainserv/<int:pk>/edit/', views.DomainServEditView.as_view(), name='domainserv_edit'),
   path('domainserv/<int:pk>/delete/', views.DomainServDeleteView.as_view(), name='domainserv_delete'),
]