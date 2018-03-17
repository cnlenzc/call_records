"""
data to test create
"""
from rest_framework import status


class Records_create():
    """
    class to define the records to test and assert
    """

    ok1 = {
        "in":
        {
            "start_time": 6,
            "end_time": 22,
            "price_per_call_standard": 0.36,
            "price_per_call_reduced": 0.36,
            "price_per_minute_standard": 0.09,
            "price_per_minute_reduced": 0,
        },
        "out":
        {
            "start_time": 6,
            "end_time": 22,
            "price_per_call_standard": "0.36",
            "price_per_call_reduced": "0.36",
            "price_per_minute_standard": "0.09",
            "price_per_minute_reduced": "0.00"
        },
        "status_code": status.HTTP_201_CREATED
    }

    ok2 = {
        "in":
        {
            "start_time": 0,
            "end_time": 20,
            "price_per_call_standard": 0.40,
            "price_per_call_reduced": 0.25,
            "price_per_minute_standard": 0.2,
            "price_per_minute_reduced": 0.05,
        },
        "out":
        {
            "start_time": 0,
            "end_time": 20,
            "price_per_call_standard": "0.40",
            "price_per_call_reduced": "0.25",
            "price_per_minute_standard": "0.20",
            "price_per_minute_reduced": "0.05"
        },
        "status_code": status.HTTP_201_CREATED
    }

    all_null = {
        "in":
        {
            "start_time": None,
            "end_time": None,
            "price_per_call_standard": None,
            "price_per_call_reduced": None,
            "price_per_minute_standard": None,
            "price_per_minute_reduced": None
        },
        "out":
        {
            "start_time": [
                "A valid integer is required."
            ],
            "end_time": [
                "A valid integer is required."
            ],
            "price_per_call_standard": [
                "A valid number is required."
            ],
            "price_per_call_reduced": [
                "A valid number is required."
            ],
            "price_per_minute_standard": [
                "A valid number is required."
            ],
            "price_per_minute_reduced": [
                "A valid number is required."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }

    invalid_price = {
        "in":
        {
            "start_time": 6,
            "end_time": 22,
            "price_per_call_standard": "1234567890123.12",
            "price_per_call_reduced": "-4.00",
            "price_per_minute_standard": "ola",
            "price_per_minute_reduced": "1e5",
        },
        "out":
        {
            "price_per_call_standard": [
                "Ensure that there are no more than 12 digits in total."
            ],
            "price_per_call_reduced": [
                "Ensure this value is greater than or equal to 0.0."
            ],
            "price_per_minute_standard": [
                "A valid number is required."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }

    invalid_hour = {
        "in":
        {
            "start_time": -1,
            "end_time": 24,
            "price_per_call_standard": 0.36,
            "price_per_call_reduced": 0.36,
            "price_per_minute_standard": 0.09,
            "price_per_minute_reduced": 0,
        },
        "out":
        {
            "start_time": [
                "Ensure this value is greater than or equal to 0."
            ],
            "end_time": [
                "Ensure this value is less than or equal to 23."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }
