from rest_framework.routers import DefaultRouter

from .views import *


app_name = 'services'

router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet)

urlpatterns = router.urls
