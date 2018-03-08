from rest_framework import serializers
from app.models import BillLine


class BillLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillLine
        fields = ('__all__')

