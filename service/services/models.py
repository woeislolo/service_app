from django.db import models
from django.core.validators import MaxValueValidator

from clients.models import *


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7,
                                decimal_places=2)
    
    def __str__(self):
        return f'{self.name} {self.price}'
    

class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )

    type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveSmallIntegerField(default=0,
                                                        validators=[
                                                            MaxValueValidator(100)
                                                        ])
    def __str__(self):
        return f'{self.type} {self.discount_percent}'
    

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)

    def get_price(self):
        return self.service.price * (100 - self.plan.discount_percent) / 100

    def __str__(self):
        return f'{self.client}, {self.service}, {self.plan}'
    