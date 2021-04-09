from rest_framework import serializers
from user.models import Money, Convertion

class MoneySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Money
        fields = ('name', 'code')

class ConvertionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Convertion
        fields = ('currency', 'to', 'rate')
