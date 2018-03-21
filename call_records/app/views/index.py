"""
Index view definition
"""
from rest_framework import viewsets, response


class IndexViewSet(viewsets.ViewSet):
    """
    Index view definition
    """

    def list(self, request, *args, **kwargs):
        """ list application links """
        resp = {
            "title": "Welcome to the system of call records!",
            "API Documentation": request.build_absolute_uri('docs'),
            "Charge price setting": request.build_absolute_uri('config-price'),
            "Calls handle": request.build_absolute_uri('call-record'),
            "Create/retrieve the bill": request.build_absolute_uri('bill'),
        }
        return response.Response(resp)
