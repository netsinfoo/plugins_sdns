from django import forms

from django.forms import IntegerField, ValidationError, widgets
from django.conf import settings

from extras.forms import (
    CustomFieldModelForm,
    CustomFieldModelCSVForm,
    AddRemoveTagsForm,
    CustomFieldModelBulkEditForm,
    CustomFieldModelFilterForm,
    CustomFieldBulkEditForm,
)

from utilities.forms import (
    BootstrapMixin,
    DynamicModelMultipleChoiceField,
    TagFilterField,
    StaticSelect,
    CSVChoiceField,
    CSVModelChoiceField,
    DynamicModelChoiceField,
    APISelect,
    CSVModelForm,
    StaticSelectMultiple,
    add_blank_choice,
)

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


#### TIPOS EXTRAS DE FORMS


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


# class RegisterBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldBulkEditForm):
#     pk = forms.ModelMultipleChoiceField(
#         queryset=Register.objects.all(),
#         widget=forms.MultipleHiddenInput()
#     )
#     domain = DynamicModelChoiceField(
#         queryset=Domain.objects.all(),
#         required=False
#     )
    
#     host = forms.CharField(
#         max_length=30,
#         required=False
#     )

#     class Meta:
#         nullable_fields = [ ]

        

# ================= DOMAIN =====================

class DomainForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = Domain
        fields = [
            'name',
            'date_joined',
            'owner',
            'domParent',
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

#### TIPOS EXTRAS DE FORMS

class DomainCSVForm(CSVModelForm):


    class Meta:
        model = Domain
        fields = Domain.csv_headers


# class DomainBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldBulkEditForm):
#     pk = forms.ModelMultipleChoiceField(
#         queryset = Domain.objects.all(),
#         widget = forms.MultipleHiddenInput()
#     )
#     domParent = DynamicModelChoiceField(
#         queryset=Domain.objects.all(),
#         required=False
#     )

#     owner = forms.CharField(
#         max_length=2,
#         required=False
#     )

#     class Meta:
#         nullable_fields = []


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
# class RespBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldBulkEditForm):
#     pk = forms.ModelMultipleChoiceField(
#         queryset = Resp.objects.all(),
#         widget = forms.MultipleHiddenInput(
#         # api_url='/api/plugins/sdns/resp'
#         )
#     )

#     tipo = forms.ChoiceField(
#         choices=add_blank_choice(RespChoices),
#         widget=StaticSelect2()
#     )

#     dom = DynamicModelChoiceField(
#         queryset= Domain.objects.all(),
#         display_field='Domain',
#         label='Dominio',
#         required= False,
#         widget= APISelect(
#             api_url='/api/plugins/sdns/domain',
#         )
#     )

#     class Meta:
#         nullable_fields = [ ]


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
