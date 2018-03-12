from rest_framework import status
from util import get_last_month

class Records_create():

    ok1 = \
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

    ok2 = \
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

    ok_2_calls = \
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
                    "start_date_time": "2018-01-30T23:02:26",
                    "duration": "08:25:55",
                    "price": "8.28"
                },
                {
                    "destination": "21980000001",
                    "start_date_time": "2018-01-31T23:59:15",
                    "duration": "00:05:10",
                    "price": "0.36"
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
                {
                    "destination": "21980000006",
                    "start_date_time": "2018-02-28T23:58:00",
                    "duration": "00:03:50",
                    "price": "0.36"
                }
            ]
        },
        "status_code": status.HTTP_201_CREATED
    }

    not_unique = \
    {
        "in": ok2["in"],
        "out": ok2["out"],
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
                "Phone number must be entered in the format: 'AAXXXXXXXXX'. Where AA is the area code and XXXXXXXXX is the phone number.",
                "Ensure this field has at least 10 characters."
            ],
            "period": [
                "Invalid period. Period must be entered in the format: 'YYYY-MM'. Where YYYY is the year and MM is the month."
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
                "Phone number must be entered in the format: 'AAXXXXXXXXX'. "
                "Where AA is the area code and XXXXXXXXX is the phone number.",
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
                "Phone number must be entered in the format: 'AAXXXXXXXXX'. "
                "Where AA is the area code and XXXXXXXXX is the phone number.",
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
                "Invalid period. Period must be entered in the format: 'YYYY-MM'. "
                "Where YYYY is the year and MM is the month."
            ]
        },
        "status_code": status.HTTP_400_BAD_REQUEST
    }

