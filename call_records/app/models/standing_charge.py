from django.db import models
from util import MyTypes


class StandingCharge(models.Model):
    price = MyTypes.PositiveMoneyField12(
        help_text = "Standing charge price per call")

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '$ %s' % (self.price)
