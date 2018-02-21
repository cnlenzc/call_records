from rest_framework import serializers
from app.models import CallRecord, START


class CallRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallRecord
        fields = ('__all__')

    def validate(self, attrs):
        """
        Check fields souce and destination.
        """
        if attrs['type'] == START:
            if not attrs['source']:
                raise serializers.ValidationError(
                    "The source field cannot be blank for call type start")
            if not attrs['destination']:
                raise serializers.ValidationError(
                    "The destination field cannot be blank for call type start")

        return attrs
