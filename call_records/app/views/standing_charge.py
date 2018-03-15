"""
Standing Charge view definition
"""
from rest_framework import viewsets, mixins, permissions, response
from app.models import StandingCharge
from app.serializers import StandingChargeSerializer


class StandingChargeViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    This viewset provides the following actions:
    list: Returns the StandingCharge.
    create: Create (or update) the StandingCharge.
    """
    queryset = StandingCharge.objects.all()
    serializer_class = StandingChargeSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset().get()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data)
        except StandingCharge.DoesNotExist:
            return response.Response({})

    def perform_create(self, serializer):
        try:
            instance = self.get_queryset().get()
            serializer.update(instance, serializer.validated_data)
        except StandingCharge.DoesNotExist:
            super().perform_create(serializer)
