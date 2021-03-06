from django.db import models

from customers.models import Customer


class Account(models.Model):
    amount = models.FloatField()


class AccountCustomer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owners')
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        unique_together = ('account', 'owner')


class TransactionTypes(models.TextChoices):
    WITHDRAW = 'WITHDRAW'


class Transaction(models.Model):
    type = models.CharField(max_length=10, choices=TransactionTypes.choices)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
