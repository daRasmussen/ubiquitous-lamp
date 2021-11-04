from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from account.models import Account


class Address(models.Model):
    address = models.CharField(max_length=30)
    building_number = models.IntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postcode = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
