from django.db import models
from util import MyTypes


class CallCharge(models.Model):
    price00h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 00h and 00h59")

    price01h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 01h and 01h59")

    price02h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 02h and 02h59")

    price03h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 03h and 03h59")

    price04h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 04h and 04h59")

    price05h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 05h and 05h59")

    price06h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 06h and 06h59")

    price07h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 07h and 07h59")

    price08h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 08h and 08h59")

    price09h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 09h and 09h59")

    price10h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 10h and 10h59")

    price11h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 11h and 11h59")

    price12h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 12h and 12h59")

    price13h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 13h and 13h59")

    price14h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 14h and 14h59")

    price15h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 15h and 15h59")

    price16h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 16h and 16h59")

    price17h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 17h and 17h59")

    price18h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 18h and 18h59")

    price19h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 19h and 19h59")

    price20h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 20h and 20h59")

    price21h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 21h and 21h59")

    price22h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 22h and 22h59")

    price23h = MyTypes.PositiveMoneyField12(
        help_text="Call charge per minute between 23h and 23h59")

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '%s' % (self.id)
