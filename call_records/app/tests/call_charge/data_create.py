from datetime import datetime
from rest_framework import status

class Records_create():

    ok1 = \
    {
        "in":
        {
            "price00h": "0",
            "price01h": "0",
            "price02h": 0,
            "price03h": "0.00",
            "price04h": "0.00",
            "price05h": "0.00",
            "price06h": 0.09,
            "price07h": "0.09",
            "price08h": "0.09",
            "price09h": "0.09",
            "price10h": "0.09",
            "price11h": "0.09",
            "price12h": "0.09",
            "price13h": "0.09",
            "price14h": "0.09",
            "price15h": "0.09",
            "price16h": "0.09",
            "price17h": "0.09",
            "price18h": "0.09",
            "price19h": "0.09",
            "price20h": "0.09",
            "price21h": 00.09,
            "price22h": "0.00",
            "price23h": "0.00"
        },
        "out":
        {
            "price00h": "0.00",
            "price01h": "0.00",
            "price02h": "0.00",
            "price03h": "0.00",
            "price04h": "0.00",
            "price05h": "0.00",
            "price06h": "0.09",
            "price07h": "0.09",
            "price08h": "0.09",
            "price09h": "0.09",
            "price10h": "0.09",
            "price11h": "0.09",
            "price12h": "0.09",
            "price13h": "0.09",
            "price14h": "0.09",
            "price15h": "0.09",
            "price16h": "0.09",
            "price17h": "0.09",
            "price18h": "0.09",
            "price19h": "0.09",
            "price20h": "0.09",
            "price21h": "0.09",
            "price22h": "0.00",
            "price23h": "0.00"
        },
        "status_code": status.HTTP_201_CREATED
    }

    ok2 = \
    {
        "in":
        {
            "price00h": "0.00",
            "price01h": "0.00",
            "price02h": "0.00",
            "price03h": "0.00",
            "price04h": "0.00",
            "price05h": "0.00",
            "price06h": "0.09",
            "price07h": "0.09",
            "price08h": "0.09",
            "price09h": "0.10",
            "price10h": "0.09",
            "price11h": "0.09",
            "price12h": "0.09",
            "price13h": "0.11",
            "price14h": "0.11",
            "price15h": "0.09",
            "price16h": "0.09",
            "price17h": "0.09",
            "price18h": "0.09",
            "price19h": "0.09",
            "price20h": "0.09",
            "price21h": "0.09",
            "price22h": "0.00",
            "price23h": "0.00"
        },
        "out":
        {
            "price00h": "0.00",
            "price01h": "0.00",
            "price02h": "0.00",
            "price03h": "0.00",
            "price04h": "0.00",
            "price05h": "0.00",
            "price06h": "0.09",
            "price07h": "0.09",
            "price08h": "0.09",
            "price09h": "0.10",
            "price10h": "0.09",
            "price11h": "0.09",
            "price12h": "0.09",
            "price13h": "0.11",
            "price14h": "0.11",
            "price15h": "0.09",
            "price16h": "0.09",
            "price17h": "0.09",
            "price18h": "0.09",
            "price19h": "0.09",
            "price20h": "0.09",
            "price21h": "0.09",
            "price22h": "0.00",
            "price23h": "0.00"
        },
        "status_code": status.HTTP_201_CREATED
    }

    all_null = \
    {
        "in":
        {
            "price00h": None,
            "price01h": None,
            "price02h": None,
            "price03h": None,
            "price04h": None,
            "price05h": None,
            "price06h": None,
            "price07h": None,
            "price08h": None,
            "price09h": None,
            "price10h": None,
            "price11h": None,
            "price12h": None,
            "price13h": None,
            "price14h": None,
            "price15h": None,
            "price16h": None,
            "price17h": None,
            "price18h": None,
            "price19h": None,
            "price20h": None,
            "price21h": None,
            "price22h": None,
            "price23h": None
        },
        "out":
        {
            "price00h": [
                "A valid number is required."
            ],
            "price01h": [
                "A valid number is required."
            ],
            "price02h": [
                "A valid number is required."
            ],
            "price03h": [
                "A valid number is required."
            ],
            "price04h": [
                "A valid number is required."
            ],
            "price05h": [
                "A valid number is required."
            ],
            "price06h": [
                "A valid number is required."
            ],
            "price07h": [
                "A valid number is required."
            ],
            "price08h": [
                "A valid number is required."
            ],
            "price09h": [
                "A valid number is required."
            ],
            "price10h": [
                "A valid number is required."
            ],
            "price11h": [
                "A valid number is required."
            ],
            "price12h": [
                "A valid number is required."
            ],
            "price13h": [
                "A valid number is required."
            ],
            "price14h": [
                "A valid number is required."
            ],
            "price15h": [
                "A valid number is required."
            ],
            "price16h": [
                "A valid number is required."
            ],
            "price17h": [
                "A valid number is required."
            ],
            "price18h": [
                "A valid number is required."
            ],
            "price19h": [
                "A valid number is required."
            ],
            "price20h": [
                "A valid number is required."
            ],
            "price21h": [
                "A valid number is required."
            ],
            "price22h": [
                "A valid number is required."
            ],
            "price23h": [
                "A valid number is required."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }

    invalid_price = \
    {
        "in":
        {
            "price00h": "123456789012.12",
            "price01h": "12345678901.12",
            "price02h": "1234567890.12",
            "price03h": "-5",
            "price04h": "-12345678901.12",
            "price05h": "1e5",
            "price06h": "e",
            "price07h": "123456789.123",
            "price08h": "-123456.123",
            "price09h": "*",
            "price10h": "1e6",
            "price11h": "1e9",
            "price12h": "1e10",
            "price13h": "1e11",
            "price14h": "1e12",
            "price15h": "1e13",
            "price16h": "0.09",
            "price17h": "0.09",
            "price18h": "0.09",
            "price19h": "0.09",
            "price20h": "0.09",
            "price21h": "0.09",
            "price22h": "0.00",
            "price23h": "0.00"
        },
        "out":
        {
            "price00h": [
                "Ensure that there are no more than 12 digits in total."
            ],
            "price01h": [
                "Ensure that there are no more than 12 digits in total."
            ],
            "price03h": [
                "Ensure this value is greater than or equal to 0.0."
            ],
            "price04h": [
                "Ensure that there are no more than 12 digits in total."
            ],
            "price06h": [
                "A valid number is required."
            ],
            "price07h": [
                "Ensure that there are no more than 2 decimal places."
            ],
            "price08h": [
                "Ensure that there are no more than 2 decimal places."
            ],
            "price09h": [
                "A valid number is required."
            ],
            "price12h": [
                "Ensure that there are no more than 10 digits before the decimal point."
            ],
            "price13h": [
                "Ensure that there are no more than 10 digits before the decimal point."
            ],
            "price14h": [
                "Ensure that there are no more than 12 digits in total."
            ],
            "price15h": [
                "Ensure that there are no more than 12 digits in total."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }



