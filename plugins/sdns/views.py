from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import View
from netbox.views import generic

from .filters import RegisterFilter, DomainFilter, RespFilter, NsFilter, MxFilter, CtsFilter, DomainServFilter
from .forms import RegisterFilterForm, RegisterForm, DomainFilterForm, DomainForm, RespFilterForm, RespForm, NsFilterForm, NsForm, MxFilterForm, MxForm, CtsFilterForm, CtsForm, DomainServFilterForm, DomainServForm
from .models import  Register, Domain, Resp, Ns, Mx, Cts, DomainServ
from .tables import RegisterTable, DomainTable, RespTable, NsTable, MxTable, CtsTable, DomainServTable
# Create your views here.
# =======================Registros========================================
class RegisterListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_register'
    queryset = Register.objects.all()
    filterset = RegisterFilter
    filterset_form = RegisterFilterForm
    table = RegisterTable
    template_name = 'sdns/register_list.html'

class RegisterCreateView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = 'sdns.add_register'
    model = Register
    queryset = Register.objects.all()
    model_form =  RegisterForm
    template_name = 'sdns/register_edit.html'
    default_return_url = 'plugins:sdns:register_list'

class RegisterBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_register'
    queryset = Register.objects.filter()
    table = RegisterTable
    default_return_url = 'plugins:sdns:register_list'

class RegisterView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class RegisterEditView(RegisterCreateView):
    permission_required = 'sdns.change_sdns'

class RegisterDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_register'
    model = Register
    default_return_url = 'plugins:sdns:register_list'

# ===========================Domain==========================================

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
    template_name = 'sdns/domain_edit.html'
    default_return_url = 'plugins:sdns:domain_list'

class DomainBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_domain'
    queryset = Domain.objects.filter()
    table = DomainTable
    default_return_url = 'plugins:sdns:domain_list'

class DomainView(View):
    """Single virtual circuits view, identified by ID."""

    def get(self, request, pk):
        vc = get_object_or_404(VirtualCircuit.objects.filter(vcid=pk))
        vlan_ids = VirtualCircuitVLAN.objects.filter(virtual_circuit=vc).values_list('vlan_id', flat=True)
        vlans = [VLAN.objects.get(pk=vid) for vid in vlan_ids]

        return render(request, 'netbox_virtual_circuit_plugin/virtual_circuit.html', {
            'virtual_circuit': vc,
            'vlans': vlans,
        })

class DomainEditView(DomainCreateView):
    permission_required = 'sdns.change_sdns'

class DomainDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_domain'
    model = Domain
    default_return_url = 'plugins:sdns:domain_list'

# ===========================Resposáveis==========================================

class RespListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = 'sdns.view_resp'
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
    template_name = 'sdns/resp_edit.html'
    default_return_url = 'plugins:sdns:resp_list'

class RespBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_resp'
    queryset = Resp.objects.filter()
    table = RespTable
    default_return_url = 'plugins:sdns:resp_list'

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

class RespEditView(RespCreateView):
    permission_required = 'sdns.change_sdns'

class RespDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = 'sdns.delete_resp'
    model = Resp
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
    template_name = 'sdns/ns_edit.html'
    default_return_url = 'plugins:sdns:ns_list'

class NsBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_ns'
    queryset = Ns.objects.filter()
    table = NsTable
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
    template_name = 'sdns/mx_edit.html'
    default_return_url = 'plugins:sdns:mx_list'

class MxBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_mx'
    queryset = Mx.objects.filter()
    table = MxTable
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
    template_name = 'sdns/cts_edit.html'
    default_return_url = 'plugins:sdns:cts_list'

class CtsBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_cts'
    queryset = Cts.objects.filter()
    table = CtsTable
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
    template_name = 'sdns/domainserv_edit.html'
    default_return_url = 'plugins:sdns:domainserv_list'

class DomainServBulkDeleteView(PermissionRequiredMixin, generic.BulkDeleteView):
    permission_required = 'sdns.delete_domainserv'
    queryset = DomainServ.objects.filter()
    table = DomainServTable
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





