from django.db import models
from django.core.validators import MinValueValidator


class StandingCharge(models.Model):
    price = models.DecimalField(
        help_text = "Standing charge price per call",
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]
        )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '$ %s' % (self.price)
