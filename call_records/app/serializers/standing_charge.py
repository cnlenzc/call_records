"""
Standing Charge serializer definition
"""
from rest_framework import serializers
from app.models import StandingCharge


class StandingChargeSerializer(serializers.ModelSerializer):
    """
    Standing Charge serializer definition
    """

    class Meta:
        model = StandingCharge
        fields = ('price',)
