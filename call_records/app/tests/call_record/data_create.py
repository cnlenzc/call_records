from datetime import datetime
from rest_framework import status

timestamp1 = int(datetime.now().timestamp())
timestamp2 = timestamp1 + 5 * 60  # 5 minutes after


class Records_create():

    ok1 = \
        {
            "in":
            {
                "type": "1",
                "timestamp": timestamp1,
                "call_id": 1,
                "source": "1636203365",
                "destination": "1699999999"
            },
            "out":
            {
                "type": "1",
                "timestamp": timestamp1,
                "call_id": 1,
                "source": "1636203365",
                "destination": "1699999999"
            },
            "status_code": status.HTTP_201_CREATED
        }

    ok2 = \
        {
            "in":
            {
                "type": "2",
                "timestamp": timestamp2,
                "call_id": 1,
            },
            "out":
            {
                "type": "2",
                "timestamp": timestamp2,
                "call_id": 1,
                "source": None,
                "destination": None,
            },
            "status_code": status.HTTP_201_CREATED
        }

    not_unique = \
        {
            "in": ok1["in"],
            "out":
            {
                "non_field_errors": [
                    "The fields call_id, type must make a unique set."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    all_blank = \
        {
            "in":
            {
                "type": "",
                "timestamp": 0,
                "call_id": 0,
                "source": "",
                "destination": ""
            },
            "out":
            {
                "type": [
                    "\"\" is not a valid choice."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    all_null = \
        {
            "in":
            {
                "type": None,
                "timestamp": None,
                "call_id": None,
                "source": None,
                "destination": None
            },
            "out":
            {
                "type": [
                    "\"None\" is not a valid choice."
                ],
                "timestamp": [
                    "A valid integer is required."
                ],
                "call_id": [
                    "A valid integer is required."
                ],
                "source": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'."
                    " Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has at least 10 characters."
                ],
                "destination": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'."
                    " Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has at least 10 characters."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    start_without_source_destination = \
        {
            "in":
            {
                "type": "1",
                "timestamp": timestamp1,
                "call_id": 1
            },
            "out":
            {
                "non_field_errors": [
                    "The source field cannot be blank for call type start",
                    "The destination field cannot be blank for call type start"
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_phone_number1 = \
        {
            "in":
            {
                "type": "1",
                "timestamp": timestamp1,
                "call_id": 1,
                "source": "123456789",
                "destination": "123456789012"
            },
            "out":
            {
                "source": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'."
                    " Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has at least 10 characters."
                ],
                "destination": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'."
                    " Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has no more than 11 characters."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_phone_number2 = \
        {
            "in":
            {
                "type": "1",
                "timestamp": timestamp1,
                "call_id": 1,
                "source": "123456789o",
                "destination": "abc",
            },
            "out":
            {
                "source": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'."
                    " Where AA is the area code and "
                    "XXXXXXXXX is the phone number."
                ],
                "destination": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'."
                    " Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has at least 10 characters."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_type = \
        {
            "in":
            {
                "type": "3",
                "timestamp": timestamp1,
                "call_id": 1,
                "source": "1636203365",
                "destination": "1699999999"
            },
            "out":
            {
                "type": [
                    "\"3\" is not a valid choice."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_timestamp_and_call_id1 = \
        {
            "in":
            {
                "type": "1",
                "timestamp": 1636203365.678,
                "call_id": -2,
                "source": "1636203365",
                "destination": "1699999999"
            },
            "out":
            {
                "timestamp": [
                    "A valid integer is required."
                ],
                "call_id": [
                    "Ensure this value is greater than or equal to 0."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_timestamp_and_call_id2 = \
        {
            "in":
            {
                "type": "1",
                "timestamp": "ola",
                "call_id": "1.56",
                "source": "1636203365",
                "destination": "1699999999"
            },
            "out":
            {
                "timestamp": [
                    "A valid integer is required."
                ],
                "call_id": [
                    "A valid integer is required."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }
