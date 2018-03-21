"""
Create a Bill and its bill lines from call records
"""
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from app.models import \
    BillLine, CallRecord, START, END, ConfigPrice


class BuildTheBill():
    """
    Create a Bill and its bill lines from call records
    """

    def __init__(self, bill):
        self._bill = bill

    def build(self):
        """ build the bill """
        self._read_config_price()
        self._timestamp_calculation()
        calls_of_period = self._read_calls_of_period()

        for call_start in calls_of_period:
            self._create_bill_line(call_start)

    def _timestamp_calculation(self):
        """ calculate the timestamp for the start and end """
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
        """ read all call of bill period """
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
        """ create a line of bill """
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
        """ price calculation of a call """

        # convert timestamp to datetime
        time_start = datetime.fromtimestamp(timestamp_start)
        time_end = datetime.fromtimestamp(timestamp_end)

        # price per call calculation
        if time_start.hour >= self._start_time and \
           time_start.hour < self._end_time:
            price = self._price_per_call_standard
        else:
            price = self._price_per_call_reduced

        time_inter = datetime(time_start.year, time_start.month,
                              time_start.day, time_start.hour, 0)
        # for each hour in the call time
        while time_inter < time_end:
            time_next = time_inter + timedelta(hours=1)
            first_minute = \
                time_inter if time_inter > time_start else time_start
            last_minute = \
                time_next if time_next < time_end else time_end
            minutes_within_the_hour = \
                (last_minute - first_minute).seconds // 60

            # price_per_minute calculation within the hour
            if time_inter.hour >= self._start_time and \
               time_inter.hour < self._end_time:
                price_per_minute = self._price_per_minute_standard
            else:
                price_per_minute = self._price_per_minute_reduced

            price += price_per_minute * minutes_within_the_hour
            time_inter = time_next
        return price

    def _read_config_price(self):
        """ read the config price """
        res = ConfigPrice.objects.filter()[:1]
        if not res.count():
            raise ValidationError(
                'The Config Price setting does not exist.')
        self._start_time = res[0].start_time
        self._end_time = res[0].end_time
        self._price_per_call_standard = res[0].price_per_call_standard
        self._price_per_call_reduced = res[0].price_per_call_reduced
        self._price_per_minute_standard = res[0].price_per_minute_standard
        self._price_per_minute_reduced = res[0].price_per_minute_reduced
