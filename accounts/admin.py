from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from accounts.models import Account, Transaction


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ('id', 'amount')


@admin.register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = ('id', 'type', 'account')
