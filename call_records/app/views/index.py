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
            "docs": request.build_absolute_uri('docs'),
            "config ": {
                "standing-charge":
                    request.build_absolute_uri('standing-charge'),
                "call-charge": request.build_absolute_uri('call-charge'),
            },
            "handles": {
                "call-record": request.build_absolute_uri('call-record'),
                "bill": request.build_absolute_uri('bill'),
            },
        }
        return response.Response(resp)
