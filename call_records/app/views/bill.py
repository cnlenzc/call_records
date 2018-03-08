from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, permissions, pagination, response
from app.models import Bill
from app.serializers import BillSerializer


class BillFilter(FilterSet):

    class Meta:
        model = Bill
        fields = ['source']


class BillPagination(pagination.PageNumberPagination):

    page_size = 25

    def get_paginated_response(self, data):
        return response.Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class BillViewSet(viewsets.ModelViewSet):
    """
    This viewset provides the following actions:
    list: Returns the bill list.
    create: Create a new bill.
    retrieve: Returns a specific bill.
    update: Update all fields in a bill.
    partial_update: Update a field from a bill.
    destroy: Remove a bill.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = BillFilter
    pagination_class = BillPagination

