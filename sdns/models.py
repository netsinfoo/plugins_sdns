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

    name = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1, choices=TIPO, null=True)
    dom =  models.ForeignKey('Domain', models.SET_NULL, blank= True, null=True, related_name='use_domain')

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['name', 'dom', 'tipo'], name='unique_resp')]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:sdns:resp_edit', kwargs={"pk": self.pk})


    csv_headers = ['name','tipo','dom']

    def to_csv(self):
        return(
            self.name,
            self.tipo,
            self.dom,
        )



class Domain(models.Model):


    OWN = [
        ('AG', 'AUDITOR GERAL'),
        ('Ag', 'AUDIROT GERAL ADJUNTO'),
        ('C',  'COODENADOR'),
        ('D',  'DIRETOR'),
        ('DA', 'DIRETOR ADJUNTO'),
        ('DC', 'DIRETOR DE CENTRO'),
        ('O',  'OUVIDOR'),
        ('OA', 'OUVIDOR ADJUNTO'),
        ('PR', 'PRO-REITOR'),
        ('Pr', 'PRO-REITOR ADJUNTO'),
        ('R',  'REITOR'),
        ('S',  'SECRETARIO'),
        ('SA', 'SECRETARIO ADJUNTO'),
        ('U',  'SUPERINTENDENTE'),
        ('UA', 'SUPERINTENDENTE ADJUNTO'),
        ('VD', 'VICE DIRETOR'),
        ('VC', 'VICE DIRETOR DE CENTRO'),
        ('VR', 'VICE-REITOR'),
    ]


    # resp = models.ForeignKey('Resp', models.SET_NULL, blank= True, null=True, related_name='resp')
    owner = models.CharField(max_length=2, choices=OWN, null=True)
    name = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField()
    domParent = models.ForeignKey('Domain',
                            models.SET_NULL,
                            blank=True,
                            null=True,
                            related_name='domParet')

    # def get_absolute_url(self):
    #     return reverse("domain_update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:sdns:domain', args={self.pk})

    csv_headers = ['owner', 'name', 'date_joined', 'domParent']

    clone_fields = ['owner', 'date_joined']

    def to_csv(self):
        return (
            self.owner,
            self.name,
            self.date_joined,
            self.domParent
        )


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

    csv_headers = ['ns', 'dom', 'tipo']

    def to_csv(self):
        return (
            self.ns,
            self.dom,
            self.tipo,
        )


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

    csv_headers = ['mx', 'dom', 'prior']

    def to_csv(self):
        return (
            self.mx,
            self.dom,
            self.prior,
        )


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



    csv_headers = ['domain', 'host', 'reg', 'ip']

    def to_csv(self):
        return (
            self.domain,
            self.host,
            self.reg,
            self.ip,
        )


class Cts(models.Model):

    REGI= [
        ('1' ,'CNAME'),
        ('2' ,'TXT'),
        ('3' ,'SPF'),
     ]

    registro =  models.ForeignKey('ipam.IPAddress', models.SET_NULL, blank= True, null=True)
    reg      = models.CharField(max_length=1, choices=REGI)
    content  = models.CharField(max_length=30)


    # def get_absolute_url(self):
    #     return reverse("cts_update", kwargs={"pk": self.pk})
    class Meta:
        constraints = [ models.UniqueConstraint(fields=['registro', 'reg', 'content'], name='unique_Cts')]

    def __str__(self):
        return self.content

    csv_headers = ['registro', 'reg', 'content']

    def to_csv(self):
        return (
            self.registro,
            self.reg,
            self.content,
        )


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

    csv_headers = ['service', 'dominio', 'relation']

    def to_csv(self):
        return (
            self.service,
            self.dominio,
            self.relation,
        )
