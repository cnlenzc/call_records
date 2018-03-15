"""
data to test retrieve
"""
from rest_framework import status
from .data_create import Records_create as recc


class Records_retrieve():
    """
    class to define the records to test and assert
    """

    ok1 = \
        {
            "create": recc.ok1,
            "out": recc.ok1['out'],
            "status_code": status.HTTP_200_OK
        }

    ok2 = \
        {
            "create": recc.ok2,
            "out": recc.ok2['out'],
            "status_code": status.HTTP_200_OK
        }

    not_found = \
        {
            "create": recc.ok2,
            "out":
            {
                "detail": "Not found."
            },
            "status_code": status.HTTP_404_NOT_FOUND
        }
