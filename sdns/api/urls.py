from rest_framework import routers
from netbox.api import OrderedDefaultRouter
from . import views
from .views import *


router = routers.DefaultRouter()
router.APIRootView = views.SdnsRootView

router.register('registers', RegisterViewSet)
router.register('resp', RespViewSet)
router.register('domainserv', DomainServViewSet)
router.register('ns', NsViewSet)
router.register('mx', MxViewSet)
router.register('cts', CtsViewSet)
router.register('domain', DomainViewSet)

app_name = 'sdns-api'
urlpatterns = router.urls