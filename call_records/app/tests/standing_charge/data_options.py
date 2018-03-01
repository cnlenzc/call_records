from rest_framework import status


class Records_options():

    ok = \
    {
        "out":
        {
            "name": "Standing Charge List",
            "renders": [
                "application/json",
                "text/html"
            ],
            "parses": [
                "application/json",
                "application/x-www-form-urlencoded",
                "multipart/form-data"
            ],
            "actions": {
                "POST": {
                    "price": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price",
                    }
                }
            }
        },
        "status_code": status.HTTP_200_OK
    }
