"""
Standing Charge view definition
"""
from rest_framework import viewsets, mixins, permissions, response
from app.models import ConfigPrice
from app.serializers import ConfigPriceSerializer


class ConfigPriceViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    This viewset provides the following actions:
    list: Returns the ConfigPrice.
    create: Create (or update) the ConfigPrice.
    """
    queryset = ConfigPrice.objects.all()
    serializer_class = ConfigPriceSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset().get()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data)
        except ConfigPrice.DoesNotExist:
            return response.Response({})

    def perform_create(self, serializer):
        try:
            instance = self.get_queryset().get()
            serializer.update(instance, serializer.validated_data)
        except ConfigPrice.DoesNotExist:
            super().perform_create(serializer)
