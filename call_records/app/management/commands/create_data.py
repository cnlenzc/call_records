"""
Command to create data for settings and test
"""
from datetime import datetime
from django.core.management.base import BaseCommand
from django.db.models import Max
from app.models import ConfigPrice, CallRecord


CONFIG_PRICE = {
    "start_time": 6,
    "end_time": 22,
    "price_per_call_standard": 0.36,
    "price_per_call_reduced": 0.36,
    "price_per_minute_standard": 0.09,
    "price_per_minute_reduced": 0,
}

LIST_CALL_RECORD = [
    ['2018-01-29', '15:00:00', 60 * 60 + 00, '88888888888', '21980000008'],
    ['2018-01-30', '23:02:26', 505 * 60 + 55, '88888888888', '21980000008'],
    ['2018-01-31', '23:59:15', 5 * 60 + 10, '88888888888', '21980000001'],
    ['2018-02-04', '18:40:15', 32 * 60 + 20, '88888888888', '21980000002'],
    ['2018-02-05', '06:40:15', 2 * 60 + 30, '88888888888', '21980000003'],
    ['2018-02-06', '21:50:25', 22 * 60 + 40, '88888888888', '21980000004'],
    ['2018-02-07', '08:00:00', 1 * 60 + 00, '88888888888', '21980000005'],
    ['2018-02-28', '23:58:00', 3 * 60 + 50, '88888888888', '21980000006'],
    ['2018-02-10', '21:57:13', 13 * 60 + 43, '1632203625', '21980000007'],
    ['2018-02-20', '09:00:20', 59, '11111111111', '21980000008'],
    ['2018-02-21', '09:00:20', 60, '11111111111', '21980000009'],
    ['2018-02-22', '09:00:20', 61, '11111111111', '21980000010'],
    ['2018-02-23', '09:00:40', 60, '11111111111', '21980000011'],
    ['2018-02-24', '09:00:00', 60, '11111111111', '21980000012'],
]


class Command(BaseCommand):
    """ Command to create data for settings and test """
    help = 'Create data for test'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        update_or_create(ConfigPrice, CONFIG_PRICE)
        create_call_list()


def update_or_create(model, data):
    """ update/create e print result """
    affected_rows = model.objects.all().update(**data)
    if affected_rows == 0:
        ret = model.objects.create(**data)
        print('create %s %s' % (model.__name__, ret))
    else:
        print('update %s %s' % (affected_rows, model.__name__))


def create_call_list():
    """ create the list of calls """
    call_id = CallRecord.objects.aggregate(
        Max('call_id'))['call_id__max'] or 0
    for item in LIST_CALL_RECORD:
        call_id += 1
        s = item[0] + 'T' + item[1]
        date_time = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
        timestamp1 = int(date_time.timestamp())
        rec1 = {
            "type": "1",
            "timestamp": timestamp1,
            "call_id": call_id,
            "source": item[3],
            "destination": item[4]
        }
        timestamp2 = timestamp1 + item[2]
        rec2 = {
            "type": "2",
            "timestamp": timestamp2,
            "call_id": call_id,
        }
        ret = CallRecord.objects.create(**rec1)
        print('create %s %s' % (CallRecord.__name__, ret))
        ret = CallRecord.objects.create(**rec2)
        print('create %s %s' % (CallRecord.__name__, ret))
