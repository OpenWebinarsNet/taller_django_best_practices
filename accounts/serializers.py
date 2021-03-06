from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import Account, Transaction, AccountCustomer
from customers.models import Customer
from customers.serializers import CustomerSerializer


class AccountSerializer(serializers.ModelSerializer):
    owners = serializers.SerializerMethodField()

    def get_owners(self, instance: Account):
        return CustomerSerializer(Customer.objects.filter(accounts__account_id=instance.pk), many=True).data

    class Meta:
        model = Account
        fields = ('id', 'amount', 'owners')


class CreateAccountSerializer(serializers.ModelSerializer):
    owners = serializers.ListField(child=serializers.IntegerField())

    def validate_owners(self, owners: list[int]):
        owners = set(owners)

        if not all(Customer.objects.filter(pk=owner).exists() for owner in owners):
            raise ValidationError('There is customer not created yet')

        return list(owners)

    def create(self, validated_data):
        account = Account.objects.create(amount=self.validated_data.get('amount'))

        for owner_id in self.validated_data.get('owners'):
            AccountCustomer.objects.create(account=account, owner_id=owner_id)

        return account

    class Meta:
        model = Account
        fields = ('amount', 'owners')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'type', 'account', 'amount')

    def save(self, **kwargs) -> Transaction:
        return Transaction.objects.create(account=self.validated_data.get('account'),
                                          type=self.validated_data.get('type'),
                                          amount=self.validated_data.get('amount'))

