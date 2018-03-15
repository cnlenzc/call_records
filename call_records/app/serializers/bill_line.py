"""
Bill line serializer definition
"""
from rest_framework import serializers
from app.models import BillLine


class BillLineSerializer(serializers.ModelSerializer):
    """
    Bill line serializer definition
    """

    class Meta:
        model = BillLine
        fields = ('__all__')


class BillLineSerializerLigth(serializers.ModelSerializer):
    """
    Bill line serializer without id and bill fields
    """

    class Meta:
        model = BillLine
        exclude = ('id', 'bill')
