"""
Call Charge serializer definition
"""
from rest_framework import serializers
from app.models import CallCharge


class CallChargeSerializer(serializers.ModelSerializer):
    """
    Call Charge serializer definition
    """

    class Meta:
        model = CallCharge
        exclude = ('id',)
