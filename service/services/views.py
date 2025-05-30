from rest_framework.viewsets import ReadOnlyModelViewSet

from django.db.models import F

from .models import *
from .serializers import *


class SubscriptionViewSet(ReadOnlyModelViewSet):
    queryset = Subscription.objects.select_related(
        'client__user',
        'plan'
        ).only(
            'client__user__username',
            'client__user__email',
            'plan__type'
            ).annotate(
                price=F('service__price') * (100 - F('plan__discount_percent')) / 100
                )
    serializer_class = SubscriptionSerializer
