"""
Config price model definition
"""
from django.db import models
from util import MyTypes


class ConfigPrice(models.Model):
    """
    Config price model definition
    """
    start_time = MyTypes.Hour(
        help_text="Start time of the standard call. e.g.: 06")

    end_time = MyTypes.Hour(
        help_text="End time of the standard call. e.g.: 20")

    price_per_call_standard = MyTypes.PositiveMoneyField12(
        help_text="Charge per call in standard period")

    price_per_call_reduced = MyTypes.PositiveMoneyField12(
        help_text="Charge per call in reduced tariff period")

    price_per_minute_standard = MyTypes.PositiveMoneyField12(
        help_text="Charge per minute in standard period")

    price_per_minute_reduced = MyTypes.PositiveMoneyField12(
        help_text="Charge per minute in reduced tariff period")

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return 'id:%s' % (self.id)
