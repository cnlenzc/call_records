from rest_framework import serializers
from app.models import StandingCharge


class StandingChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StandingCharge
        fields = ('price',)
