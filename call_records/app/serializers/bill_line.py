from rest_framework import serializers
from app.models import BillLine


class BillLineSerializerLigth(serializers.ModelSerializer):

    class Meta:
        model = BillLine
        exclude = ('id', 'bill')


class BillLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillLine
        fields = ('__all__')

