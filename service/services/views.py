from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import *
from .serializers import *


class SubscriptionViewSet(ReadOnlyModelViewSet):
    queryset = Subscription.objects.select_related('client__user', 'plan').only(
        'client__user__username',
        'client__user__email',
        'plan__type',
    )
    serializer_class = SubscriptionSerializer
