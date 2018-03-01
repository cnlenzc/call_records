from datetime import datetime
from rest_framework import status

class Records_create():

    ok1 = \
    {
        "in":
        {
            "price": "0.36"
        },
        "out":
        {
            "price": "0.36"
        },
        "status_code": status.HTTP_201_CREATED
    }

    ok2 = \
    {
        "in":
        {
            "price": "1234567890.12"
        },
        "out":
        {
            "price": "1234567890.12"
        },
        "status_code": status.HTTP_201_CREATED
    }

    all_null = \
    {
        "in":
        {
            "price": None
        },
        "out":
        {
            "price": [
                "A valid number is required."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }

    invalid_price = \
    {
        "in":
        {
            "price": "1234567890123.12"
        },
        "out":
        {
            "price": [
                "Ensure that there are no more than 12 digits in total."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }

    invalid_price2 = \
    {
        "in":
        {
            "price": "-4.00",
        },
        "out":
        {
            "price": [
                "Ensure this value is greater than or equal to 0.0."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }





