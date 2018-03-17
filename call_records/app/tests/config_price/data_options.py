"""
data to test options
"""
from rest_framework import status


class Records_options():
    """
    class to define the records to test and assert
    """

    ok = {
        "out":
        {
            "name": "Config Price List",
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
                    "start_time": {
                        "type": "integer",
                        "required": True,
                        "read_only": False,
                        "label": "Start time",
                        "min_value": 0,
                        "max_value": 23
                    },
                    "end_time": {
                        "type": "integer",
                        "required": True,
                        "read_only": False,
                        "label": "End time",
                        "min_value": 0,
                        "max_value": 23
                    },
                    "price_per_call_standard": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price per call standard",
                        "min_value": 0.0
                    },
                    "price_per_call_reduced": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price per call reduced",
                        "min_value": 0.0
                    },
                    "price_per_minute_standard": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price per minute standard",
                        "min_value": 0.0
                    },
                    "price_per_minute_reduced": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price per minute reduced",
                        "min_value": 0.0
                    }
                }
            }
        },
        "status_code": status.HTTP_200_OK
    }
