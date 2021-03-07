from django.db import models

from accounts.models.accounts import Account


class TransactionTypes(models.TextChoices):
    WITHDRAW = 'WITHDRAW'


class Transaction(models.Model):
    type = models.CharField(max_length=10, choices=TransactionTypes.choices)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
