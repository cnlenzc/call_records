"""
Bill line serializer definition
"""
from rest_framework import serializers
from app.models import BillLine


class BillLineSerializerLigth(serializers.ModelSerializer):
    """
    Bill line serializer without id and bill fields
    """

    class Meta:
        model = BillLine
        exclude = ('id', 'bill')
