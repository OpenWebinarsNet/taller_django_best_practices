from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from accounts.models import Account, Transaction, AccountCustomer


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ('id', 'amount')


@admin.register(AccountCustomer)
class AccountCustomerAdmin(ModelAdmin):
    list_display = ('id', 'account', 'owner')


@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ('id', 'type', 'account')
