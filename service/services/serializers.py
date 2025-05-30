from rest_framework import serializers

from .models import *


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('type',)


class SubscriptionSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.user.username')
    email = serializers.CharField(source='client.user.email')
    plan = PlanSerializer()
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        # return obj.get_price()
        return obj.price

    class Meta:
        model = Subscription
        fields = ('id', 'client_name', 'email', 'service', 'plan', 'price')
