from rest_framework import viewsets, response


class IndexViewSet(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        resp = \
        {
            "title": "Welcome to the system of call records!",
            "docs": request.build_absolute_uri('docs'),
            "config ": {
                "standing-charge": request.build_absolute_uri('standing-charge'),
                "call-charge": request.build_absolute_uri('call-charge'),
            },
            "handles": {
                "call-record": request.build_absolute_uri('call-record'),
                "bill": request.build_absolute_uri('bill'),
                "bill-line": request.build_absolute_uri('bill-line'),
            },
        }
        return response.Response(resp)



