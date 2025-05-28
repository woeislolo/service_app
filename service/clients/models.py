from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = 'Companies'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user}, {self.company}'

