from rest_framework import routers
from .views import RegisterViewSet

router = routers.DefaultRouter()
router.register('registers', RegisterViewSet)
urlpatterns = router.urls