from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50)
    account = serializers.IntegerField()
    amount = serializers.FloatField()

    class Meta:
        fields = ('id', 'type', 'account', 'amount')
