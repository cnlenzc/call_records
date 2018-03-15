"""
Call Charge view definition
"""
from rest_framework import viewsets, mixins, permissions, response
from app.models import CallCharge
from app.serializers import CallChargeSerializer


class CallChargeViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    This viewset provides the following actions:
    list: Returns the CallCharge.
    create: Create (or update) the CallCharge.
    """
    queryset = CallCharge.objects.all()
    serializer_class = CallChargeSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset().get()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data)
        except CallCharge.DoesNotExist:
            return response.Response({})

    def perform_create(self, serializer):
        try:
            instance = self.get_queryset().get()
            serializer.update(instance, serializer.validated_data)
        except CallCharge.DoesNotExist:
            super().perform_create(serializer)
