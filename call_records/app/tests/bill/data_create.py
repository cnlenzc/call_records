"""
data to test create
"""
from rest_framework import status
from util import get_last_month


class Records_create():
    """
    class to define the records to test and assert
    """

    ok_no_calls = \
        {
            "in":
            {
                "source": "1636203366",
                "period": "2018-02",
            },
            "out":
            {
                "source": "1636203366",
                "period": "2018-02",
                "calls": []
            },
            "status_code": status.HTTP_201_CREATED
        }

    ok_no_calls_and_default_period = \
        {
            "in":
            {
                "source": "1636203365",
            },
            "out":
            {
                "source": "1636203365",
                "period": get_last_month(),
                "calls": []
            },
            "status_code": status.HTTP_201_CREATED
        }

    ok_1_call = \
        {
            "in":
            {
                "source": "99999999999",
                "period": "2018-02",
            },
            "out":
            {
                "source": "99999999999",
                "period": "2018-02",
                "calls": [
                    {
                        "destination": "21980000007",
                        "start_date_time": "2018-02-10T21:57:13",
                        "duration": "00:13:43",
                        "price": "0.54"
                    }
                ]
            },
            "status_code": status.HTTP_201_CREATED
        }

    ok_end_of_call_out_of_period = \
        {
            "in":
            {
                "source": "88888888888",
                "period": "2018-01",
            },
            "out":
            {
                "source": "88888888888",
                "period": "2018-01",
                "calls": [
                    {
                        "destination": "21980000008",
                        "start_date_time": "2018-01-29T15:00:00",
                        "duration": "01:00:00",
                        "price": "5.76"
                    },
                    {
                        "destination": "21980000008",
                        "start_date_time": "2018-01-30T23:02:26",
                        "duration": "08:25:55",
                        "price": "8.28"
                    }
                ]
            },
            "status_code": status.HTTP_201_CREATED
        }

    ok_5_calls = \
        {
            "in":
            {
                "source": "88888888888",
                "period": "2018-02",
            },
            "out":
            {
                "source": "88888888888",
                "period": "2018-02",
                "calls": [
                    {
                        "destination": "21980000001",
                        "start_date_time": "2018-01-31T23:59:15",
                        "duration": "00:05:10",
                        "price": "0.36"
                    },
                    {
                        "destination": "21980000002",
                        "start_date_time": "2018-02-04T18:40:15",
                        "duration": "00:32:20",
                        "price": "3.15"
                    },
                    {
                        "destination": "21980000003",
                        "start_date_time": "2018-02-05T06:40:15",
                        "duration": "00:02:30",
                        "price": "0.54"
                    },
                    {
                        "destination": "21980000004",
                        "start_date_time": "2018-02-06T21:50:25",
                        "duration": "00:22:40",
                        "price": "1.17"
                    },
                    {
                        "destination": "21980000005",
                        "start_date_time": "2018-02-07T08:00:00",
                        "duration": "00:01:00",
                        "price": "0.45"
                    },
                ]
            },
            "status_code": status.HTTP_201_CREATED
        }

    ok_near_60seg = \
        {
            "in":
            {
                "source": "11111111111",
                "period": "2018-02",
            },
            "out":
            {
                "source": "11111111111",
                "period": "2018-02",
                "calls": [
                    {
                        "destination": "21980000008",
                        "start_date_time": "2018-02-20T09:00:20",
                        "duration": "00:00:59",
                        "price": "0.36"
                    },
                    {
                        "destination": "21980000009",
                        "start_date_time": "2018-02-21T09:00:20",
                        "duration": "00:01:00",
                        "price": "0.45"
                    },
                    {
                        "destination": "21980000010",
                        "start_date_time": "2018-02-22T09:00:20",
                        "duration": "00:01:01",
                        "price": "0.45"
                    },
                    {
                        "destination": "21980000011",
                        "start_date_time": "2018-02-23T09:00:40",
                        "duration": "00:01:00",
                        "price": "0.45"
                    },
                    {
                        "destination": "21980000012",
                        "start_date_time": "2018-02-24T09:00:00",
                        "duration": "00:01:00",
                        "price": "0.45"
                    }
                ]
            },
            "status_code": status.HTTP_201_CREATED
        }

    not_unique = \
        {
            "in": ok_no_calls["in"],
            "out": ok_no_calls["out"],
            "status_code": status.HTTP_200_OK
        }

    all_blank = \
        {
            "in":
            {
                "source": "",
                "period": "",
            },
            "out":
            {
                "source": [
                    "This field may not be blank."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    all_null = \
        {
            "in":
            {
                "source": None,
                "period": None
            },
            "out":
            {
                "source": [
                    "Phone number must be entered in the format:"
                    " 'AAXXXXXXXXX'."
                    " Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has at least 10 characters."
                ],
                "period": [
                    "Invalid period. Period must be entered in the format: "
                    "'YYYY-MM'. Where YYYY is the year and MM is the month."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_phone_number1 = \
        {
            "in":
            {
                "source": "ola",
            },
            "out":
            {
                "source": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'. "
                    "Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has at least 10 characters."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_phone_number2 = \
        {
            "in":
            {
                "source": "123456789012",
            },
            "out":
            {
                "source": [
                    "Phone number must be entered in the format: "
                    "'AAXXXXXXXXX'. "
                    "Where AA is the area code and "
                    "XXXXXXXXX is the phone number.",
                    "Ensure this field has no more than 11 characters."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_period_date = \
        {
            "in":
            {
                "source": "1636203366",
                "period": "2018-00",
            },
            "out":
            {
                "period": [
                    "Invalid period. The period must be a valid year-month."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_period_future = \
        {
            "in":
            {
                "source": "1636203366",
                "period": "2999-01",
            },
            "out":
            {
                "period": [
                    "Invalid period: year-month must be in the past."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }

    invalid_period_format = \
        {
            "in":
            {
                "source": "1636203366",
                "period": "ola",
            },
            "out":
            {
                "period": [
                    "Invalid period. Period must be entered in the format: "
                    "'YYYY-MM'. "
                    "Where YYYY is the year and MM is the month."
                ]
            },
            "status_code": status.HTTP_400_BAD_REQUEST
        }
