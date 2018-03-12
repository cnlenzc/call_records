from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.db import transaction
from rest_framework.response import Response
from rest_framework import viewsets, permissions, mixins, pagination, status, response, exceptions
from app.models import Bill, BillLine, CallRecord, START, END
from app.serializers import BillSerializer
from app.business_rules import BuildTheBill
from util import get_last_month


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


class BillViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    This viewset provides the following actions:
    list: Returns the bill list.
    create: Create a new bill.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = BillFilter
    pagination_class = BillPagination


    def create(self, request, *args, **kwargs):
        '''
        rewriting the create method.
        if the object exists, then do not create, just retrieve.
        '''
        try:
            source = request.data.get('source', '')
            period = request.data.get('period', '')
            if period == '':
                period = get_last_month()
            # trying to get the instance with the same key
            instance = self.get_queryset().get(source=source, period=period)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Bill.DoesNotExist:
            # if the instance does not exist, then create
            return super().create(request, *args, **kwargs)


    def perform_create(self, serializer):
        '''
        rewriting the perform_create method.
        creating all the lines of the bill.
        '''
        # This operation must be atomic (doing everything or nothing)
        with transaction.atomic():
            super().perform_create(serializer)
            BuildTheBill(serializer.instance).build()

