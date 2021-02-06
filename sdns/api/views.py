from rest_framework.viewsets import ModelViewSet
from sdns.models import Register, Domain, Resp, Ns, Mx, Cts, DomainServ
from .serializers import RegisterSerializer, DomainSerializer, RespSerializer, NsSerializer, MxSerializer, CtsSerializer, DomainServSerializer

class RegisterViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class DomainViewSet(ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class RespViewSet(ModelViewSet):
    queryset = Resp.objects.all()
    serializer_class = RespSerializer

class NsViewSet(ModelViewSet):
    queryset = Ns.objects.all()
    serializer_class = NsSerializer

class MxViewSet(ModelViewSet):
    queryset = Mx.objects.all()
    serializer_class = MxSerializer

class CtsViewSet(ModelViewSet):
    queryset = Cts.objects.all()
    serializer_class = CtsSerializer

class DomainServViewSet(ModelViewSet):
    queryset = DomainServ.objects.all()
    serializer_class = DomainServSerializer
