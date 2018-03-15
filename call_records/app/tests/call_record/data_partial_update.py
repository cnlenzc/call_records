"""
data to test partial_update
"""
from rest_framework import status
from .data_create import Records_create as recc


class Records_partial_update():
    """
    class to define the records to test and assert
    """

    ok1 = \
        {
            "create": recc.ok2,
            "in": {
                "timestamp": recc.ok1['in']['timestamp'],
            },
            "out": {
                "type": recc.ok2['in']['type'],
                "timestamp": recc.ok1['in']['timestamp'],
                "call_id": recc.ok2['in']['call_id'],
                "source": None,
                "destination": None
            },
            "status_code": status.HTTP_200_OK
        }

    not_found = \
        {
            "create": recc.ok2,
            "in": {
                "timestamp": recc.ok1['in']['timestamp'],
            },
            "out":
            {
                "detail": "Not found."
            },
            "status_code": status.HTTP_404_NOT_FOUND
        }

    not_unique = \
        {
            "create": [
                recc.ok1,
                recc.ok2
            ],
            "in": {
                "type": recc.ok1['in']['type'],
            },
            "out":
            {
                "non_field_errors": [
                    "The fields call_id, type must make a unique set."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }
