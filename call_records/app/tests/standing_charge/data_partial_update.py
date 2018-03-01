from rest_framework import status
from .data_create import Records_create as recc


class Records_partial_update():

    ok1 = \
    {
        "create": recc.ok2,
        "in": {
            "price": recc.ok1['in']['price']
        },
        "out": None,
        "status_code": status.HTTP_404_NOT_FOUND
    }
