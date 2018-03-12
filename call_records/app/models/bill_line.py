from django.db import models
from util import MyTypes
from app.models.bill import Bill


class BillLine(models.Model):

    bill = models.ForeignKey(
        Bill,
        help_text = "The bill informations",
        related_name='calls',
        on_delete=models.CASCADE)

    destination = MyTypes.PhoneNumber11(
        help_text = "The phone number receiving the call")

    start_date_time = models.DateTimeField(
        help_text = "start date time: e.g. 2018-03-01 14:32")

    duration = models.DurationField(
        help_text = "call duration (hour, minute and seconds): e.g. 0:35:42 ")

    price = MyTypes.PositiveMoneyField12(
        help_text = "call price: e.g. 3.96 ")

    class Meta:
        indexes = [
            models.Index(
                fields=['bill', 'start_date_time'],
                name='bill_startdatetime_idx'),
        ]
        unique_together = ('bill', 'start_date_time')
        ordering = ('bill', 'start_date_time')

    def __str__(self):
        return 'bill:%s start_date_time:%s' % \
               (self.bill, self.start_date_time)


