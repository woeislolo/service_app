from django.contrib import admin

from .models import *


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'discount_percent')
    list_display_links = ('id', 'type', 'discount_percent')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'service', 'plan')
    list_display_links = ('id', 'client', 'service', 'plan')
