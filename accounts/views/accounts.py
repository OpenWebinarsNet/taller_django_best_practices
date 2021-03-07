# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from accounts.models import Account
from accounts.models.accounts import AccountCustomer
from accounts.serializers.accounts import ListAccountSerializer, CreateAccountSerializer


class AccountViewset(ViewSet):

    def list(self, request):
        accounts = Account.objects.all()

        serializer = ListAccountSerializer(accounts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = CreateAccountSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data.get('amount')
        account = Account.objects.create(amount=amount)

        owners = serializer.validated_data.get('owners')
        for owner_id in owners:
            AccountCustomer.objects.create(account=account, owner_id=owner_id)

        account_serializer = ListAccountSerializer(account)
        return Response(data=account_serializer.data, status=status.HTTP_201_CREATED)
