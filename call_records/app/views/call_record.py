"""
Call view definition
"""
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import \
    viewsets, permissions, pagination, response, exceptions
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

    def create(self, request, *args, **kwargs):
        '''
        Override the create method.
        if the object exists, then do not create, just update.
        '''
        try:
            return super().create(request, *args, **kwargs)
        except exceptions.ValidationError as error:
            # verify that the validation error is not unique
            if 'unique' in error.get_codes().get('non_field_errors', []):
                # There is an instance, so update
                call_id = request.data.get('call_id', None)
                type_field = request.data.get('type', None)
                # trying to get the instance with the same unique pair
                self.current_instance = \
                    self.get_queryset().get(call_id=call_id, type=type_field)
                return super().update(request, *args, **kwargs)
            else:
                raise error

    def get_object(self):
        """
        Returns the object
        Override method to use in create method (update without pk)
        """
        if getattr(self, 'current_instance', None):
            ret = self.current_instance
        else:
            ret = super().get_object()
        return ret
