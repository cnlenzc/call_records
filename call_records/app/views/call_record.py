from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, permissions
from app.models import CallRecord
from app.serializers import CallRecordSerializer


class CallRecordFilter(FilterSet):

    class Meta:
        model = CallRecord
        fields = ['call_id', 'source']


class CallRecordViewSet(viewsets.ModelViewSet):
    """
    This viewset provides the following actions:
    list: Returns the call list.
    create: Create a new call.
    retrieve: Returns a specific call.
    update: Update all fields in a call.
    partial_update: Update a field from a call.
    destroy: Remove a call.
    """
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = CallRecordFilter
