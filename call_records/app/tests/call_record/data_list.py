from rest_framework import status
from .data_create import Records_create as recc


class Records_list():

    list_ok = \
    {
        "create": [
            recc.ok1,
            recc.ok2
        ],
        "out":
        {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                recc.ok1['out'],
                recc.ok2['out']
            ]
        },
        "status_code": status.HTTP_200_OK
    }

    list_empty = \
    {
        "create": [],
        "out":
        {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        },
        "status_code": status.HTTP_200_OK
    }


