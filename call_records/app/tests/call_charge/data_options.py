from rest_framework import status


class Records_options():

    ok = {
        "out":
        {
            "name": "Call Charge List",
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
                    "price00h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price00h",
                        "min_value": 0.0
                    },
                    "price01h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price01h",
                        "min_value": 0.0
                    },
                    "price02h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price02h",
                        "min_value": 0.0
                    },
                    "price03h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price03h",
                        "min_value": 0.0
                    },
                    "price04h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price04h",
                        "min_value": 0.0
                    },
                    "price05h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price05h",
                        "min_value": 0.0
                    },
                    "price06h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price06h",
                        "min_value": 0.0
                    },
                    "price07h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price07h",
                        "min_value": 0.0
                    },
                    "price08h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price08h",
                        "min_value": 0.0
                    },
                    "price09h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price09h",
                        "min_value": 0.0
                    },
                    "price10h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price10h",
                        "min_value": 0.0
                    },
                    "price11h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price11h",
                        "min_value": 0.0
                    },
                    "price12h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price12h",
                        "min_value": 0.0
                    },
                    "price13h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price13h",
                        "min_value": 0.0
                    },
                    "price14h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price14h",
                        "min_value": 0.0
                    },
                    "price15h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price15h",
                        "min_value": 0.0
                    },
                    "price16h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price16h",
                        "min_value": 0.0
                    },
                    "price17h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price17h",
                        "min_value": 0.0
                    },
                    "price18h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price18h",
                        "min_value": 0.0
                    },
                    "price19h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price19h",
                        "min_value": 0.0
                    },
                    "price20h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price20h",
                        "min_value": 0.0
                    },
                    "price21h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price21h",
                        "min_value": 0.0
                    },
                    "price22h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price22h",
                        "min_value": 0.0
                    },
                    "price23h": {
                        "type": "decimal",
                        "required": True,
                        "read_only": False,
                        "label": "Price23h",
                        "min_value": 0.0
                    }
                }
            }
        },
        "status_code": status.HTTP_200_OK
    }
