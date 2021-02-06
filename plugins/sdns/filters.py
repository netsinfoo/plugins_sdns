import django_filters
from django.db.models import Q

from utilities.filters import NameSlugSearchFilterSet, BaseFilterSet

from sdns.models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ


class RegisterFilter(BaseFilterSet,NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    domain = django_filters.CharFilter( 
        method = 'filter_domain',
        label = 'Dominio'
    )
    
    host =  django_filters.CharFilter(
        method = 'filter_host',
        label = 'Host'
    )
    
    ip =  django_filters.CharFilter(
        method = 'filter_ip',
        label = 'Ip'
    ) 
   

    class Meta:
        model = Register
        fields = [
            'ip',
            'host',
            'domain',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(ip__icontains=value)
            | Q(host__icontains=value)
            | Q(domain__icontains=value)
        )

        return queryset.filter(qs_filter)

    def filter_domain(self, queryset, name, value):
        try:
            return queryset.filter(domain=(value))
        except ValidationError:
            return queryset.none()
        
    def filter_ip(self, queryset, name, value):
        
        try:
            query = str(netaddr.IPNetwork(value).cidr)
            return queryset.filter(ip=(value))
        except ValidationError:
            return queryset.none()

    def filter_host(self, queryset, name, value):
        try:
            return queryset.filter(host=(value))
        except ValidationError:
            return queryset.none()

# ============= DOMAIN ==========================

class DomainFilter(BaseFilterSet,NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    owner =  django_filters.CharFilter(
        method = 'filter_owner',
        label = 'Proprietario'
    )
    
    name =  django_filters.CharFilter(
        method = 'filter_name',
        label = 'Nome'
    )
    

    class Meta:
        model = Register
        fields = [
            'owner',
            'name',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(ip__icontains=value)
            | Q(host__icontains=value)
            | Q(domain__icontains=value)
        )

        return queryset.filter(qs_filter)

    def filter_onwer(self, queryset, name, value):
        try:
            return queryset.filter(owner=(value))
        except ValidationError:
            return queryset.none()
        
    
    def filter_name(self, queryset, name, value):
        try:
            return queryset.filter(name=(value))
        except ValidationError:
            return queryset.none()

# ============= Resp ==========================

class RespFilter(BaseFilterSet,NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    name =  django_filters.CharFilter(
        method = 'filter_name',
        label = 'Nome do dominio'
    )
    
    tipo =  django_filters.CharFilter(
        method = 'filter_tipo',
        label = 'Tipo de dominio'
    )

    dom =  django_filters.CharFilter(
        method = 'filter_dom',
        label = 'nome de dominio'
    )
    

    class Meta:
        model = Register
        fields = [
            'dom',
            'name',
            'tipo',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(name__icontains=value)
            | Q(tipo__icontains=value)
            | Q(dom__icontains=value)
        )

        return queryset.filter(qs_filter)

    def filter_name(self, queryset, name, value):
        try:
            return queryset.filter(name=(value))
        except ValidationError:
            return queryset.none()
        
    
    def filter_dom(self, queryset, name, value):
        try:
            return queryset.filter(dom=(value))
        except ValidationError:
            return queryset.none()
            
# ============= Ns ==========================

class NsFilter(BaseFilterSet,NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    ns =  django_filters.CharFilter(
        method = 'filter_ns',
        label = 'Nome do dominio'
    )
    
    tipo =  django_filters.CharFilter(
        method = 'filter_tipo',
        label = 'Tipo de dominio'
    )

    dom =  django_filters.CharFilter(
        method = 'filter_dom',
        label = 'nome de dominio'
    )
    

    class Meta:
        model = Register
        fields = [
            'dom',
            'ns',
            'tipo',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(ns__icontains=value)
            | Q(tipo__icontains=value)
            | Q(dom__icontains=value)
        )

        return queryset.filter(qs_filter)

    def filter_ns(self, queryset, name, value):
        try:
            return queryset.filter(ns=(value))
        except ValidationError:
            return queryset.none()
        
    
    def filter_dom(self, queryset, name, value):
        try:
            return queryset.filter(dom=(value))
        except ValidationError:
            return queryset.none()

    def filter_tipo(self, queryset, name, value):
        try:
            return queryset.filter(tipo=(value))
        except ValidationError:
            return queryset.none()

# ============= Mx ==========================

class MxFilter(BaseFilterSet,NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    mx =  django_filters.CharFilter(
        method = 'filter_mx',
        label = 'Nome do dominio'
    )
    
    prior =  django_filters.CharFilter(
        method = 'filter_prior',
        label = 'Tipo de prioridade'
    )

    dom =  django_filters.CharFilter(
        method = 'filter_dom',
        label = 'nome de dominio'
    )
    

    class Meta:
        model = Register
        fields = [
            'dom',
            'mx',
            'prior',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(mx__icontains=value)
            | Q(prior__icontains=value)
            | Q(dom__icontains=value)
        )

        return queryset.filter(qs_filter)

    def filter_mx(self, queryset, name, value):
        try:
            return queryset.filter(mx=(value))
        except ValidationError:
            return queryset.none()
        
    
    def filter_dom(self, queryset, name, value):
        try:
            return queryset.filter(dom=(value))
        except ValidationError:
            return queryset.none()

    def filter_prior(self, queryset, name, value):
        try:
            return queryset.filter(prior=(value))
        except ValidationError:
            return queryset.none()

# ============= Cts ==========================

class CtsFilter(BaseFilterSet,NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    registro =  django_filters.CharFilter(
        method = 'filter_registro',
        label = 'Ip do registro'
    )
    
    reg =  django_filters.CharFilter(
        method = 'filter_reg',
        label = 'Tipo de registro'
    )

    content =  django_filters.CharFilter(
        method = 'filter_content',
        label = 'Registro'
    )
    

    class Meta:
        model = Cts
        fields = [
            'registro',
            'reg',
            'content',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(registro__icontains=value)
            | Q(reg__icontains=value)
            | Q(content__icontains=value)
        )

        return queryset.filter(qs_filter)

    def filter_registro(self, queryset, name, value):
        try:
            return queryset.filter(registro=(value))
        except ValidationError:
            return queryset.none()
        
    
    def filter_reg(self, queryset, name, value):
        try:
            return queryset.filter(reg=(value))
        except ValidationError:
            return queryset.none()

# =============DomainServ ==========================

class DomainServFilter(BaseFilterSet,NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    service =  django_filters.CharFilter(
        method = 'filter_service',
        label = 'Nome do serviço'
    )
    
    dominio =  django_filters.CharFilter(
        method = 'filter_dominio',
        label = 'Dominio'
    )

    relation =  django_filters.CharFilter(
        method = 'filter_relation',
        label = 'Tipo de Relação'
    )
    

    class Meta:
        model = DomainServ
        fields = [
            'service',
            'dominio',
            'relation',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(service__icontains=value)
            | Q(dominio__icontains=value)
            | Q(relation__icontains=value)
        )

        return queryset.filter(qs_filter)

    def filter_service(self, queryset, name, value):
        try:
            return queryset.filter(service=(value))
        except ValidationError:
            return queryset.none()
        
    
    def filter_dominio(self, queryset, name, value):
        try:
            return queryset.filter(dominio=(value))
        except ValidationError:
            return queryset.none()

    def filter_relation(self, queryset, name, value):
        try:
            return queryset.filter(relation=(value))
        except ValidationError:
            return queryset.none()


