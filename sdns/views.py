from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import View
from netbox.views import generic

from utilities.paginator import EnhancedPaginator, get_paginate_count

from .filters import RegisterFilter, DomainFilter, RespFilter, NsFilter, MxFilter, CtsFilter, DomainServFilter

from .forms import RegisterFilterForm, RegisterForm, DomainFilterForm, DomainForm, RespFilterForm, RespForm, NsFilterForm, NsForm, MxFilterForm, MxForm, CtsFilterForm, CtsForm, DomainServFilterForm, DomainServForm, RespCSVForm, RegisterCSVForm, DomainCSVForm, NsCSVForm, MxCSVForm, CtsCSVForm, DomainServCSVForm, RespBulkEditForm, RegisterBulkEditForm, DomainBulkEditForm

from .models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ,  IPAddress


from .tables import RegisterTable, DomainTable, RespTable, NsTable, MxTable, CtsTable, DomainServTable, DomcTable, NsdTable, MxdTable, RegisterdTable, CtscTable

from django_tables2 import RequestConfig


# Create your views here.
# =======================Registros========================================
class RegisterView(PermissionRequiredMixin, generic.ObjectView):
    """Single virtual circuits view, identified by ID."""
    permission_required = 'sdns.add_register'
    queryset = Register.objects.all()

    def get_extra_context(self, request, instance):
        #Registros A/AAAA
        
        reg_A = Register.objects.get(host=str(instance).split(
            ".")[0]).ip
        cts_host = str(reg_A)
        #Registros CNAME
        #ip_host = str(reg_A).split("/")[0]

        regcname = IPAddress.objects.get(address=cts_host).cts_set.filter(reg=1)
        regctable = CtscTable(regcname, orderable=False)

        #Registros CNAME
        regtxt = IPAddress.objects.get(address=cts_host).cts_set.filter(reg=2)
        regttable = CtscTable(regtxt, orderable=False)

        regspf = IPAddress.objects.get(address=cts_host).cts_set.filter(reg=3)
        regstable = CtscTable(regspf, orderable=False)
   
        return {
             'reg_A' : reg_A,
             'regctable': regctable,
             'regttable': regttable,
             'regstable': regstable, 
             }


        
class RegisterListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_register'
    queryset = Register.objects.filter()
    filterset = RegisterFilter
    filterset_form = RegisterFilterForm
    table = RegisterTable
    template_name = 'sdns/register_list.html'

class RegisterCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_register'
    model = Register
    queryset = Register.objects.all()
    model_form =  RegisterForm
    # template_name = 'sdns/register_edit.html'
    default_return_url = 'plugins:sdns:register_list'

class RegisterEditView(RegisterCreateView):
    permission_required = 'sdns.change_sdns'
    
class RegisterDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_register'
    queryset = Register.objects.all()
    default_return_url = 'plugins:sdns:register_list'

#
#                   ====== REGISTER BULK VIEWS=======
#

class RegisterBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'sdns.add_register'
    queryset = Register.objects.all()
    model_form = RegisterCSVForm
    table = RegisterTable
    default_return_url = 'plugins:sdns:register_list'


class RegisterBulkEditView(PermissionRequiredMixin, generic.BulkEditView):
    permission_required = 'sdns.change_register'
    queryset = Register.objects.filter()
    filterset = RegisterFilter
    table = RegisterTable
    form = RegisterBulkEditForm
    default_return_url = 'plugins:sdns:register_list'
   

class RegisterBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_register'
    queryset = Register.objects.filter()
    table = RegisterTable
    default_return_url = 'plugins:sdns:register_list'


# ===========================Domain==========================================
class DomainView(PermissionRequiredMixin, generic.ObjectView):
    """Single virtual circuits view, identified by ID."""
    permission_required = 'sdns.add_domain'
    queryset = Domain.objects.all()
   


    def get_extra_context(self, request, instance):
        #Domains suport information
        owner_dom = Resp.objects.filter(dom=instance, tipo='D').order_by('name').first()
        owner_tec = Resp.objects.filter(dom=instance, tipo='T').order_by('name').first()

        #Ns information
        records_ns = Ns.objects.filter(dom=instance).prefetch_related('ns','dom')
        Ns_table = NsdTable(records_ns, orderable=False)

        #Mx information
        records_mx = Mx.objects.filter(dom=instance).prefetch_related('mx','dom')
        Mx_table = MxdTable(records_mx, orderable=False)

        # Address records informations
        records_ip = Register.objects.filter(domain=instance).prefetch_related('ip','domain')
        Ip_table = RegisterdTable(records_ip, orderable=False)

        # Domains children
        domc=Domain.objects.filter(domParent=instance)
        Domc_table = DomcTable(domc, orderable=False)

        # paginate = {
        #     'paginator_class': EnhancedPaginator,
        #     'per_page': get_paginate_count(request)
        # }
        
        # RequestConfig(request, paginate).configure(Ip_table)


        return {
            'owner_dom': owner_dom,
            'owner_tec': owner_tec,
            'Mx_table': Mx_table,
            'Ns_table': Ns_table,
            'Ip_table': Ip_table,
            'Domc_table': Domc_table,
        }

class DomainListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_domain'
    queryset = Domain.objects.all()
    filterset = DomainFilter
    filterset_form = DomainFilterForm
    table = DomainTable
    template_name = 'sdns/domain_list.html'

class DomainCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_domain'
    model = Domain
    queryset = Domain.objects.all()
    model_form =  DomainForm
    #template_name = 'sdns/domain_edit.html'
    default_return_url = 'plugins:sdns:domain_list'

class DomainEditView(DomainCreateView):
    permission_required = 'sdns.change_sdns'

class DomainDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_domain'
    queryset = Domain.objects.all()
    default_return_url = 'plugins:sdns:domain_list'

#
#                   ====== DOMAIN BULK VIEWS=======
#

class DomainBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'sdns.add_domain'
    queryset = Domain.objects.all()
    model_form = DomainCSVForm
    table = DomainTable
    default_return_url = 'plugins:sdns:domain_list'

class DomainBulkEditView(PermissionRequiredMixin, generic.BulkEditView):
    permission_required = 'sdns.change_domain'
    queryset = Domain.objects.filter()
    filterset = DomainFilter
    table = DomainTable
    form = DomainBulkEditForm
    default_return_url = 'plugins:sdns:domain_list'

class DomainBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_domain'
    queryset = Domain.objects.filter()
    table = DomainTable
    default_return_url = 'plugins:sdns:domain_list'


# ===========================Resposáveis==========================================
class RespView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class RespListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.add_resp'
    queryset = Resp.objects.all()
    filterset = RespFilter
    filterset_form = RespFilterForm
    table = RespTable
    template_name = 'sdns/resp_list.html'

class RespCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_resp'
    model = Resp
    queryset = Resp.objects.all()
    model_form =  RespForm
    default_return_url = 'plugins:sdns:resp_list'

class RespEditView(RespCreateView):
    permission_required = 'sdns.change_sdns'
   
class RespDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_resp'
    queryset = Resp.objects.all()
    default_return_url = 'plugins:sdns:resp_list'

#
#                   ====== RESPONSE BULK VIEWS=======
#

class RespBulkImportView(PermissionRequiredMixin,generic.BulkImportView):
    permission_required = 'sdns.add_resp'
    queryset = Resp.objects.all()
    form = RespCSVForm
    table = RespTable
    default_return_url = 'plugins:sdns:resp_list'

class RespBulkEditView(PermissionRequiredMixin, generic.BulkEditView):
    permission_required = 'sdns.add_resp'
    queryset = Resp.objects.all()
    filterset = RespFilter
    table = RespTable
    form = RespBulkEditForm
    # template_name = 'sdns/resp_bulk_edit.html'
    default_return_url = 'plugins:sdns:resp_list'

class RespBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_resp'
    queryset = Resp.objects.all()
    table = RespTable
    default_return_url = 'plugins:sdns:resp_list'

# ===========================Ns==========================================

class NsListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_ns'
    queryset = Ns.objects.all()
    filterset = NsFilter
    filterset_form = NsFilterForm
    table = NsTable
    template_name = 'sdns/ns_list.html'

class NsCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_ns'
    model = Ns
    queryset = Ns.objects.all()
    model_form =  NsForm
    # template_name = 'sdns/ns_edit.html'
    default_return_url = 'plugins:sdns:ns_list'

class NsView(View):
    """Single virtual circuits view, identified by ID."""
    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class NsEditView(NsCreateView):
    permission_required = 'sdns.change_sdns'

class NsDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_ns'
    model = Ns
    default_return_url = 'plugins:sdns:ns_list'


#
#                   ====== NAME SERVER BULK VIEWS=======
#

class NsBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'sdns.add_resp'
    queryset = Ns.objects.all()
    model_form = NsCSVForm
    table = NsTable
    default_return_url = 'plugins:sdns:ns_list'

class NsBulkEditView(PermissionRequiredMixin, generic.BulkEditView):
    permission_required = 'sdns.edit_resp'
    queryset = Ns.objects.all()
    filterset = NsFilter
    table = NsTable
    form = NsForm
    default_return_url = 'plugins:sdns:ns_list'

class NsBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_ns'
    queryset = Ns.objects.filter()
    table = NsTable
    default_return_url = 'plugins:sdns:ns_list'

# ===========================Mx==========================================

class MxListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_mx'
    queryset = Mx.objects.all()
    filterset = MxFilter
    filterset_form = MxFilterForm
    table = MxTable
    template_name = 'sdns/mx_list.html'

class MxCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_mx'
    model = Mx
    queryset = Mx.objects.all()
    model_form =  MxForm
    # template_name = 'sdns/mx_edit.html'
    default_return_url = 'plugins:sdns:mx_list'

class MxView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class MxEditView(MxCreateView):
    permission_required = 'sdns.change_sdns'

class MxDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_mx'
    model = Mx
    default_return_url = 'plugins:sdns:mx_list'

#
#                   ======BULK VIEWS=======
#

class MxBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'sdns.add_resp'
    queryset = Mx.objects.all()
    model_form = MxCSVForm
    table = MxTable
    default_return_url = 'plugins:sdns:mx_list'

class MxBulkEditView(PermissionRequiredMixin, generic.BulkEditView):
    permission_required = 'sdns.edit_resp'
    queryset = Mx.objects.all()
    filterset = MxFilter
    table = MxTable
    form = MxForm
    default_return_url = 'plugins:sdns:mx_list'

class MxBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_mx'
    queryset = Mx.objects.filter()
    table = MxTable
    default_return_url = 'plugins:sdns:mx_list'
# ===========================Cts==========================================

class CtsListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_cts'
    queryset = Cts.objects.all()
    filterset = CtsFilter
    filterset_form = CtsFilterForm
    table = CtsTable
    template_name = 'sdns/cts_list.html'

class CtsCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_cts'
    model = Cts
    queryset = Cts.objects.all()
    model_form =  CtsForm
    # template_name = 'sdns/cts_edit.html'
    default_return_url = 'plugins:sdns:cts_list'

class CtsView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class CtsEditView(CtsCreateView):
    permission_required = 'sdns.change_sdns'

class CtsDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_cts'
    model = Cts
    default_return_url = 'plugins:sdns:cts_list'

#
#                   ====== CNAME, TXT, SPF BULK VIEWS=======
#

class CtsBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'sdns.add_resp'
    queryset = Cts.objects.all()
    model_form = CtsCSVForm
    table = CtsTable
    default_return_url = 'plugins:sdns:Cts_list'

class CtsBulkEditView(PermissionRequiredMixin, generic.BulkEditView):
    permission_required = 'sdns.edit_resp'
    queryset = Cts.objects.all()
    filterset = CtsFilter
    table = CtsTable
    form = CtsForm
    default_return_url = 'plugins:sdns:Cts_list'

class CtsBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_cts'
    queryset = Cts.objects.filter()
    table = CtsTable
    default_return_url = 'plugins:sdns:cts_list'

# ===========================DomainServ==========================================

class DomainServListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_domainserv'
    queryset = DomainServ.objects.all()
    filterset = DomainServFilter
    filterset_form = DomainServFilterForm
    table = DomainServTable
    template_name = 'sdns/domainserv_list.html'

class DomainServCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_domainserv'
    model = DomainServ
    queryset = DomainServ.objects.all()
    model_form =  DomainServForm
    #template_name = 'sdns/domainserv_edit.html'
    default_return_url = 'plugins:sdns:domainserv_list'

class DomainServView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class DomainServEditView(DomainServCreateView):
    permission_required = 'sdns.change_sdns'

class DomainServDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_domainserv'
    model = DomainServ
    default_return_url = 'plugins:sdns:domainserv_list'

#
#                   ======BULK VIEWS=======
#


class DomainServBulkImportView(PermissionRequiredMixin, generic.BulkImportView):
    permission_required = 'sdns.add_resp'
    queryset = DomainServ.objects.all()
    model_form = DomainServCSVForm
    table = DomainServTable
    default_return_url = 'plugins:sdns:domainserv_list'

class DomainServBulkEditView(PermissionRequiredMixin, generic.BulkEditView):
    permission_required = 'sdns.edit_resp'
    queryset = DomainServ.objects.all()
    filterset = DomainServFilter
    table = DomainServTable
    form = DomainServForm
    default_return_url = 'plugins:sdns:domainserv_list'

class DomainServBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_domainserv'
    queryset = DomainServ.objects.filter()
    table = DomainServTable
    default_return_url = 'plugins:sdns:domainserv_list'
