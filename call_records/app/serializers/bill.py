from rest_framework import serializers
from app.models import Bill
from .bill_line import BillLineSerializerLigth


class BillSerializer(serializers.ModelSerializer):

    calls = BillLineSerializerLigth(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ('id', 'source', 'period', 'calls')

