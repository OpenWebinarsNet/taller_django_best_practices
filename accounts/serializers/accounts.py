from rest_framework import serializers


class ListAccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    amount = serializers.FloatField()

    class Meta:
        fields = ('id', 'amount')


class CreateAccountSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    owners = serializers.ListField(child=serializers.IntegerField())

    def validate_owners(self, owners: list[int]):
        owners = set(owners)
        return list(owners)

    class Meta:
        fields = ('amount', 'owners')


