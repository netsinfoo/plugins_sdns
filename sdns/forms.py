from django import forms
from extras.forms import AddRemoveTagsForm, CustomFieldBulkEditForm, CustomFieldModelCSVForm, CustomFieldModelForm, CustomFieldFilterForm

from utilities.forms import BootstrapMixin, CSVChoiceField, CSVModelChoiceField, CSVModelForm

from sdns.models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ

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
            'host',
            'domain',
        ]

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
            'date_joined',
            'owner',
        ]

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

        #==========================
        #    Bulks
        #====================


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
            'tipo',
            'dom',
        ]

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
            'prior',
            'dom',
        ]

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
            'reg',
            'content',
        ]

# ================= RESP =====================

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
            'service',
            'dominio',
            'relation',
        ]
