"""
Standing Charge serializer definition
"""
from rest_framework import serializers
from app.models import ConfigPrice


class ConfigPriceSerializer(serializers.ModelSerializer):
    """
    Standing Charge serializer definition
    """

    class Meta:
        model = ConfigPrice
        exclude = ('id',)
