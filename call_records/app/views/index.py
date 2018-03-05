from rest_framework import viewsets, response


class IndexViewSet(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        resp = \
        {
            "title": "Welcome to the system of call records!",
            "docs": {
                "link": request.build_absolute_uri('docs'),
            },
            "config standing-charge": {
                "link": request.build_absolute_uri('standing-charge'),
            },
            "config call-charge": {
                "link": request.build_absolute_uri('call-charge'),
            },
            "handles the call record": {
                "link": request.build_absolute_uri('call-record'),
            },
        }
        return response.Response(resp)



