from django.db import transaction
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from accounts.models import Account, Transaction, TransactionTypes
from accounts.serializers import AccountSerializer, TransactionSerializer, CreateAccountSerializer


class AccountViewset(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'create':
            serializer_class = CreateAccountSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)

        serializer.is_valid(raise_exception=True)
        account: Account = serializer.save()

        account_serializer = AccountSerializer(account)
        return Response(data=account_serializer.data, status=status.HTTP_201_CREATED)


class TransactionViewset(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer: Serializer = self.get_serializer_class()(data=request.data)

        serializer.is_valid(raise_exception=True)

        type_ = serializer.validated_data.get('type')
        amount = serializer.validated_data.get('amount')
        account: Account = serializer.validated_data.get('account')

        if type_ == TransactionTypes.WITHDRAW.value:
            account.amount -= amount
            account.save()

        self.perform_create(serializer)

        return Response(status=status.HTTP_201_CREATED)







