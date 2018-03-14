from rest_framework import status
from .data_create import Records_create as recc


class Records_destroy():

    ok1 = \
        {
            "create": recc.ok1,
            "out": None,
            "status_code": status.HTTP_204_NO_CONTENT
        }

    ok2 = \
        {
            "create": recc.ok2,
            "out": None,
            "status_code": status.HTTP_204_NO_CONTENT
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
