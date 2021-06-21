from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router = DefaultRouter()
router.APIRootView = views.SdnsPluginRootView

#==== REGISTROS
router.register('registers', RegisterViewSet)
router.register('resp', RespViewSet)
router.register('domainserv', DomainServViewSet)
router.register('ns', NsViewSet)
router.register('mx', MxViewSet)
router.register('cts', CtsViewSet)
router.register('domain', DomainViewSet)

app_name = 'sdns-api'
urlpatterns = router.urls

