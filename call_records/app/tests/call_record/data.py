from datetime import datetime


timestamp1 = int(datetime.now().timestamp())
timestamp2 = timestamp1 + 5 * 60  # 5 minutes before

rec1 = \
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
}


rec2 = \
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
}


