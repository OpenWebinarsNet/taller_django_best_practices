from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ViewSet, GenericViewSet

from accounts.models import Account, TransactionTypes, Transaction
from accounts.serializers.transactions import TransactionSerializer


class TransactionViewset(GenericViewSet):

    def list(self, request):
        serializer = TransactionSerializer(Transaction.objects.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = TransactionSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        type_ = serializer.validated_data.get('type')
        amount: float = serializer.validated_data.get('amount')
        account: Account = serializer.validated_data.get('account')

        if type_ == TransactionTypes.WITHDRAW.value:
            account.withdraw(amount)
            account.save()

        Transaction.objects.create(type=type_, amount=amount, account=account)

        return Response(status=status.HTTP_201_CREATED)
