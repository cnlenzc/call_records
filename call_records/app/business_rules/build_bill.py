from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from app.models import \
    BillLine, CallRecord, START, END, StandingCharge, CallCharge


class BuildTheBill():

    def __init__(self, bill):
        self._bill = bill

    def build(self):
        self._standing_charge = self._read_standing_charge()
        self._call_charge = self._read_call_charge()
        self._timestamp_calculation()
        calls_of_period = self._read_calls_of_period()

        for call_start in calls_of_period:
            self._create_bill_line(call_start)

    def _read_standing_charge(self):
        list = StandingCharge.objects.filter()[:1]
        if len(list) != 1:
            raise ValidationError(
                'The Standing Charge setting does not exist.')
        return list[0].price

    def _read_call_charge(self):
        list = CallCharge.objects.filter()[:1]
        if len(list) != 1:
            raise ValidationError('The Call Charge setting does not exist.')
        return list[0]

    def _timestamp_calculation(self):
        year, month = self._bill.period.split('-')[:2]
        # first day of the period
        period_start = datetime(int(year), int(month), 1, 0, 0)
        # first day after the period
        period_end = datetime(
            period_start.year + (period_start.month // 12),
            ((period_start.month % 12) + 1),
            1, 0, 0)
        # anticipating the start because a call may end in the given period
        period_start_anticipating = period_start - timedelta(days=7)
        self.timestamp_start = int(period_start.timestamp())
        self.timestamp_start_anticipating = \
            int(period_start_anticipating.timestamp())
        self.timestamp_end = int(period_end.timestamp())

    def _read_calls_of_period(self):
        calls = CallRecord.objects\
            .filter(
                source=self._bill.source,
                type=START,
                timestamp__range=(self.timestamp_start_anticipating,
                                  self.timestamp_end))\
            .order_by('source', 'timestamp')\
            .values('timestamp', 'destination', 'call_id')

        return calls

    def _create_bill_line(self, call_start):
        call_end = CallRecord.objects \
            .filter(call_id=call_start['call_id'], type=END) \
            .values('timestamp')

        if call_end.count() == 0:
            # ignoring endless record
            return

        call_end = call_end[0]

        if call_end['timestamp'] < self.timestamp_start or\
           call_end['timestamp'] >= self.timestamp_end:
            # ignoring the record when the end is out of period
            return

        seconds = call_end['timestamp'] - call_start['timestamp']
        duration = timedelta(seconds=seconds)
        price = self._price_calculation(call_start['timestamp'],
                                        call_end['timestamp'])

        BillLine.objects.create(
            bill=self._bill,
            destination=call_start['destination'],
            start_date_time=datetime.fromtimestamp(call_start['timestamp']),
            duration=duration,
            price=price)

    def _price_calculation(self, timestamp_start, timestamp_end):
        start = datetime.fromtimestamp(timestamp_start)
        end = datetime.fromtimestamp(timestamp_end)
        price = self._standing_charge
        time_inter = datetime(start.year, start.month,
                              start.day, start.hour, 0)
        while time_inter < end:
            time_next = time_inter + timedelta(hours=1)
            first_minute = time_inter if time_inter > start else start
            last_minute = time_next if time_next < end else end
            minutes_within_the_hour = \
                (last_minute - first_minute).seconds // 60
            name_field = 'price%02dh' % time_inter.hour
            price_per_minute = getattr(self._call_charge, name_field)
            price += price_per_minute * minutes_within_the_hour
            time_inter = time_next
        return price
