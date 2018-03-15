"""
Call view definition
"""
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, permissions, pagination, response
from app.models import CallRecord
from app.serializers import CallRecordSerializer


class CallRecordFilter(FilterSet):
    """
    Call Filter definition
    """

    class Meta:
        model = CallRecord
        fields = ['call_id', 'source']


class CallRecordPagination(pagination.PageNumberPagination):
    """
    Call Pagination definition
    """

    page_size = 25

    def get_paginated_response(self, data):
        return response.Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


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
    pagination_class = CallRecordPagination
