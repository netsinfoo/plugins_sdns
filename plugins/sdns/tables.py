import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn

from sdns.models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ


class RegisterTable(BaseTable):
    pk = ToggleColumn()
    ip = tables.LinkColumn(
        viewname='plugins:sdns:register_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Register
        fields = (
            'pk',
            'ip',
            'host',
            'domain',
        )

# ============ DOMAIN ==========================

class DomainTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:sdns:domain_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Domain
        fields = (
            'pk',
            'name',
            'date_joined',
            'owner',
        )

# ============ Resp ==========================

class RespTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:sdns:resp_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Resp
        fields = (
            'pk',
            'name',
            'tipo',
            'dom',
        )

# ============ Ns ==========================

class NsTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:sdns:ns_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Ns
        fields = (
            'pk',
            'ns',
            'tipo',
            'dom',
        )

# ============ Mx ==========================

class MxTable(BaseTable):
    pk = ToggleColumn()
    mx = tables.LinkColumn(
        viewname='plugins:sdns:mx_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Mx
        fields = (
            'pk',
            'mx',
            'prior',
            'dom',
        )

# ============ Cts ==========================

class CtsTable(BaseTable):
    pk = ToggleColumn()
    registro = tables.LinkColumn(
        viewname='plugins:sdns:cts_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = Resp
        fields = (
            'pk',
            'registro',
            'reg',
            'content',
        )


# ============ DomainServ ==========================

class DomainServTable(BaseTable):
    pk = ToggleColumn()
    service = tables.LinkColumn(
        viewname='plugins:sdns:domainserv_edit',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = DomainServ
        fields = (
            'pk',
            'service',
            'dominio',
            'relation',
        )
