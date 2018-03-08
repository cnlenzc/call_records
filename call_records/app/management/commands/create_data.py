from django.core.management.base import BaseCommand
from django.db.models import Max
from app.models import StandingCharge, CallCharge, CallRecord
from datetime import datetime


STANDING_CHARGE = {
    "price": 0.36,
}

CALL_CHARGE = {
    "price00h": 0,
    "price01h": 0,
    "price02h": 0,
    "price03h": 0,
    "price04h": 0,
    "price05h": 0,
    "price06h": 0.09,
    "price07h": 0.09,
    "price08h": 0.09,
    "price09h": 0.09,
    "price10h": 0.09,
    "price11h": 0.09,
    "price12h": 0.09,
    "price13h": 0.09,
    "price14h": 0.09,
    "price15h": 0.09,
    "price16h": 0.09,
    "price17h": 0.09,
    "price18h": 0.09,
    "price19h": 0.09,
    "price20h": 0.09,
    "price21h": 0.09,
    "price22h": 0,
    "price23h": 0,
}


LIST_CALL_RECORD = [
    ['2018-01-31', '23:59:15',  5 * 60, '16990000001', '21980000001'],
    ['2018-02-04', '18:40:15', 32 * 60, '16990000001', '21980000002'],
    ['2018-02-05', '06:40:15',  2 * 60, '16990000001', '21980000003'],
    ['2018-02-06', '21:50:25', 22 * 60, '16990000001', '21980000004'],
    ['2018-02-07', '08:00:00',      88, '16990000001', '21980000005'],
    ['2018-02-28', '23:58:00',  3 * 60, '16990000001', '21980000006'],
]


class Command(BaseCommand):
    help = 'Create data for test'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.update_or_create(StandingCharge, STANDING_CHARGE)
        self.update_or_create(CallCharge, CALL_CHARGE)
        self.create_call_list()

    def update_or_create(self, model, data):
        affected_rows = model.objects.all().update(**data)
        if affected_rows == 0:
            ret = model.objects.create(**data)
            print('create %s %s' % (model.__name__, ret))
        else:
            print('update %s %s' % (affected_rows, model.__name__))

    def create_call_list(self):
        call_id = CallRecord.objects.all().aggregate(Max('call_id')).get('call_id__max', 0)
        for item in LIST_CALL_RECORD:
            call_id += 1
            str = item[0] + 'T' + item[1]
            date_time = datetime.strptime(str, "%Y-%m-%dT%H:%M:%S")
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


