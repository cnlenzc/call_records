from rest_framework import status
from .data_create import Records_create as recc


class Records_update():

    ok1 = {
        "create": recc.ok2,
        "in": recc.ok1['in'],
        "out": recc.ok1['out'],
        "status_code": status.HTTP_200_OK
    }

    not_found = {
        "create": recc.ok1,
        "in": recc.ok1['in'],
        "out":
        {
            "detail": "Not found."
        },
        "status_code": status.HTTP_404_NOT_FOUND
    }

    not_unique = {
        "create": [
            recc.ok1,
            recc.ok2
        ],
        "in": recc.ok1["in"],
        "out": {
            "non_field_errors": [
                "The fields call_id, type must make a unique set."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }
