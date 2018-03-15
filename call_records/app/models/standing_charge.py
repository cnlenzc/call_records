"""
Standing charge model definition
"""
from django.db import models
from util import MyTypes


class StandingCharge(models.Model):
    """
    Standing charge model definition
    """
    price = MyTypes.PositiveMoneyField12(
        help_text="Standing charge price per call")

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '$ %s' % (self.price)
