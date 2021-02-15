from django import forms

from extras.forms import AddRemoveTagsForm, CustomFieldBulkEditForm, CustomFieldModelCSVForm, CustomFieldModelForm, CustomFieldFilterForm

from utilities.forms import BootstrapMixin, CSVChoiceField, CSVModelChoiceField, CSVModelForm, add_blank_choice, DynamicModelChoiceField, StaticSelect2Multiple, StaticSelect2, APISelectMultiple, DynamicModelMultipleChoiceField, APISelect, BulkEditForm, form_from_model

from sdns.models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ

from ipam.models import IPAddress, Service

from sdns.choices import *

BLANK_CHOICE = (("", "---------"),)


class RegisterForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Register
        fields = [
            'ip',
            'host',
            'domain',
        ]

class RegisterFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )

    class Meta:
        model = Register
        fields = [
            'ip',
            # 'host',
            # 'domain',
        ]




class RegisterCSVForm(CSVModelForm):
    dom = CSVModelChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        to_field_name='name',
        help_text="Dominio Dns)")


    ip = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        to_field_name='IP',
        help_text="Registro A/AAAA)")

    class Meta:
        model = Register
        fields = Register.csv_headers

# ================= DOMAIN =====================

class DomainForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Domain
        fields = [
            'name',
            'date_joined',
            'owner',
        ]

class DomainFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )

    class Meta:
        model = Domain
        fields = [
            'name',
            # 'date_joined',
            # 'owner',
        ]


class DomainCSVForm(CSVModelForm):


    class Meta:
        model = Domain
        fields = Domain.csv_headers


# ================= RESP =====================


class RespForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Resp
        fields = [
            'name',
            'tipo',
            'dom',
        ]

class RespFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )

    class Meta:
        model = Resp
        fields = [
            'name',
            # 'tipo',
            # 'dom',
        ]

#=======================================================
#               BULK
#=======================================================
class RespBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset = Resp.objects.all(),
        widget = forms.MultipleHiddenInput(
        # api_url='/api/plugins/sdns/resp'
        )
    )

    tipo = forms.ChoiceField(
        choices=add_blank_choice(RespChoices),
        widget=StaticSelect2()
    )

    dom = DynamicModelChoiceField(
        queryset= Domain.objects.all(),
        display_field='Domain',
        label='Dominio',
        required= False,
        widget= APISelect(
            api_url='/api/plugins/sdns/domain',
        )
    )

    class Meta:
        nullable_fields = [ ]


class RespCSVForm(CSVModelForm):
    dom = CSVModelChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        to_field_name='name',
        help_text="Dominio Dns)"
    )

    class Meta:
        model = Resp
        fields = Resp.csv_headers

# ================= Ns =====================

class NsForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Ns
        fields = [
            'ns',
            'tipo',
            'dom',
        ]

class NsFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )

    class Meta:
        model = Ns
        fields = [
            'ns',
            # 'tipo',
            # 'dom',
        ]

class NsCSVForm(CSVModelForm):
    ns = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        to_field_name='IP',
        help_text="Registro A/AAAA)")

    dom = CSVModelChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        to_field_name='name',
        help_text="Dominio Dns)")

    class Meta:
        model = Ns
        fields = Ns.csv_headers




# ================= Mx =====================

class MxForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Mx
        fields = [
            'mx',
            'prior',
            'dom',
        ]

class MxFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )

    class Meta:
        model = Mx
        fields = [
            'mx',
            # 'prior',
            # 'dom',
        ]

class MxCSVForm(CSVModelForm):
    mx = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        to_field_name='IP',
        help_text="Registro A/AAAA)")

    dom = CSVModelChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        to_field_name='name',
        help_text="Dominio Dns)")

    class Meta:
        model = Mx
        fields = Mx.csv_headers

# ================= Cts =====================

class CtsForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Cts
        fields = [
            'registro',
            'reg',
            'content',
        ]

class CtsFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )

    class Meta:
        model = Cts
        fields = [
            'registro',
            # 'reg',
            # 'content',
        ]

class CtsCSVForm(CSVModelForm):
    registro = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        to_field_name='IP',
        help_text="Registro A/AAAA")

    class Meta:
        model = Cts
        fields = Cts.csv_headers


# ================= DomainServ =====================
class DomainServForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = DomainServ
        fields = [
            'service',
            'dominio',
            'relation',
        ]

class DomainServFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )

    class Meta:
        model = DomainServ
        fields = [
            # 'service',
            'dominio',
            # 'relation',
        ]

class DomainServCSVForm(CSVModelForm):
    service = CSVModelChoiceField(
        queryset=Service.objects.all(),
        required=False,
        to_field_name='Serviço',
        help_text="Serviço do modulo ipam")

    dominio = CSVModelChoiceField(
        queryset=Domain.objects.all(),
        required=False,
        to_field_name='name',
        help_text="Dominio Dns")

    class Meta:
        model = DomainServ
        fields = DomainServ.csv_headers