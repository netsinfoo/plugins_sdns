from django.db import models
from django.urls import reverse
from ipam.models import IPAddress, Service
#from .choices import RegisterStatusChoices

# Create your models here.
class Resp(models.Model):
    TIPO= [
        ('D', 'DONO'),
        ('T', 'TECNICO'),
    ]

    name = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=1, choices=TIPO, null=True)
    dom =  models.ForeignKey('Domain', models.SET_NULL, blank= True, null=True, related_name='use_domain')

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['name', 'dom', 'tipo'], name='unique_resp')]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("resp_update", kwargs={"pk": self.pk})

class Domain(models.Model):


    OWN = [
        ('D', 'DIRETOR'),
        ('C', 'COODENADOR'),
        ('S', 'SECRETARIO'),
        ('U', 'SUPERINTENDENTE'),
    ]


    # resp = models.ForeignKey('Resp', models.SET_NULL, blank= True, null=True, related_name='resp')
    owner = models.CharField(max_length=1, choices=OWN, null=True)
    name = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField()

    # def get_absolute_url(self):
    #     return reverse("domain_update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

class Ns(models.Model):
    TIPO = [('M' , 'Master'), ('S', 'Slave')]

    # ns =  models.OneToOneField(
    #     to='ipam.IPAddress',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     blank=True,
    #     null=True,
    #     verbose_name='Ip NS'
    # )
    ns = models.ForeignKey('ipam.IPAddress', models.SET_NULL, blank= True, null=True)
    dom = models.ForeignKey('Domain', models.SET_NULL, blank= True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO, null=True)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['ns', 'dom'], name='unique_ns')]

    def __str__(self):
        return self.tipo

class Mx(models.Model):
    mx =  models.ForeignKey('ipam.IPAddress', models.SET_NULL, blank= True, null=True)
    # models.OneToOneField(
    #     to='ipam.IPAddress',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     blank=True,
    #     null=True,
    #     verbose_name='Ip Mx'
    # )
    dom = models.ForeignKey('Domain', models.SET_NULL, blank= True, null=True)
    prior = models.CharField(max_length=2,null=True)


    class Meta:
        constraints = [ models.UniqueConstraint(fields=['mx', 'dom'], name='unique_,mx')]

    def __str__(self):
        return self.prior

class Register(models.Model):
    REG= [
        ('1' , 'A'),
        ('2' ,'AAAA'),
     ]

    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    host   = models.CharField(max_length=30)
    reg    = models.CharField(max_length=1, choices=REG)
    ip     = models.ForeignKey('ipam.IPAddress', models.SET_NULL, blank= True, null=True)
    # models.OneToOneField(
    #     to='ipam.IPAddress',
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     blank=True,
    #     null=True,
    #     verbose_name='IP host'
    # )


    class Meta:
        constraints = [ models.UniqueConstraint(fields=['host', 'domain'], name='unique_register')]


    def __str__(self):
        return self.host +"."+ str(self.domain)

class Cts(models.Model):

    REGI= [
        ('1' ,'CNAME'),
        ('2' ,'TXT'),
        ('3' ,'SPF'),
     ]

    registro =  models.ForeignKey('ipam.IPAddress', models.SET_NULL, blank= True, null=True)
    reg      = models.CharField(max_length=1, choices=REGI)
    content  = models.CharField(max_length=30)


    def get_absolute_url(self):
        return reverse("cts_update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.content


# class Service(models.Model):
#     nome = models.CharField(max_length=30)
#     dispositivo = models.CharField(max_length=30, unique=True)

#     def __str__(self):
#         return self.dispositivo

class DomainServ(models.Model):
    REL = [
        ('P', 'PRIMARIO'),
        ('S', 'SECUNDARIO'),
        ('T', 'TERCEARIO'),
    ]

    service = models.ForeignKey('ipam.Service', on_delete=models.CASCADE)
    dominio = models.ForeignKey('Domain',  on_delete=models.CASCADE)
    relation = models.CharField(max_length=1, choices=REL)

