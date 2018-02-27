from rest_framework import status


class Records_options():

    ok = \
    {
        "out":
        {
            "name": "Call Record List",
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
                    "id": {
                        "type": "integer",
                        "required": False,
                        "read_only": True,
                        "label": "ID"
                    },
                    "type": {
                        "type": "choice",
                        "required": True,
                        "read_only": False,
                    },
                    "timestamp": {
                        "type": "integer",
                        "required": True,
                        "read_only": False,
                        "min_value": 0,
                        "max_value": 2147483647
                    },
                    "call_id": {
                        "type": "integer",
                        "required": True,
                        "read_only": False,
                        "min_value": 0,
                        "max_value": 2147483647
                    },
                    "source": {
                        "type": "string",
                        "required": False,
                        "read_only": False,
                        "min_length": 10,
                        "max_length": 11
                    },
                    "destination": {
                        "type": "string",
                        "required": False,
                        "read_only": False,
                        "min_length": 10,
                        "max_length": 11
                    }
                }
            }
        },
        "status_code": status.HTTP_200_OK
    }
