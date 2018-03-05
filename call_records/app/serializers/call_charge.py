from rest_framework import serializers
from app.models import CallCharge


class CallChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallCharge
        exclude = ('id',)
