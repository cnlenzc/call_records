"""
Call Record serializer definition
"""
from rest_framework import serializers
from app.models import CallRecord, START


class CallRecordSerializer(serializers.ModelSerializer):
    """
    Call Record serializer definition
    """

    class Meta:
        model = CallRecord
        fields = ('__all__')

    def validate(self, attrs):
        """
        Check fields souce and destination.
        """
        msgs = []
        if attrs.get('type', None) == START:
            if not attrs.get('source', None):
                msgs.append("The source field cannot be blank "
                            "for call type start")
            if not attrs.get('destination', None):
                msgs.append("The destination field cannot be "
                            "blank for call type start")
        if msgs:
            raise serializers.ValidationError(msgs)

        return attrs
