from django.db import models
from util import MyTypes, get_last_month


class Bill(models.Model):

    source = MyTypes.PhoneNumber11(
        help_text = "The subscriber phone number that originated the call")

    period = MyTypes.PeriodYearMonth(
        help_text = "The reference period (month/year) (optional)",
        default=get_last_month)

    class Meta:
        indexes = [models.Index(fields=['source', 'period'])]
        unique_together = ('source', 'period')
        ordering = ('source', 'period')

    def __str__(self):
        return 'source:%s period:%s' % \
               (self.source, self.period)



