from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, permissions, pagination, response
from app.models import BillLine
from app.serializers import BillLineSerializer


class BillLineFilter(FilterSet):

    class Meta:
        model = BillLine
        fields = ['bill']


class BillLinePagination(pagination.PageNumberPagination):

    page_size = 25

    def get_paginated_response(self, data):
        return response.Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class BillLineViewSet(viewsets.ModelViewSet):
    """
    This viewset provides the following actions:
    list: Returns the BillLine list.
    create: Create a new BillLine.
    retrieve: Returns a specific BillLine.
    update: Update all fields in a BillLine.
    partial_update: Update a field from a BillLine.
    destroy: Remove a BillLine.
    """
    queryset = BillLine.objects.all()
    serializer_class = BillLineSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = BillLineFilter
    pagination_class = BillLinePagination

