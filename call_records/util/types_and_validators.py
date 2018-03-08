from functools import partial
import datetime
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from .funcs import get_last_month


PhoneNumber11_regex = RegexValidator(
    regex=r'^\d{10,11}$',
    message="Phone number must be entered in the format: 'AAXXXXXXXXX'. "
            "Where AA is the area code and XXXXXXXXX is the phone number.")


def PeriodYearMonth_validate(value):
    regex = RegexValidator(
        regex=r'^\d{4}-\d{2}$',
        message="Invalid period. Period must be entered in the format: 'YYYY-MM'. "
                "Where YYYY is the year and MM is the month.")
    regex(value)

    try:
        year, month = value.split('-')[:2]
        datetime.date(int(year), int(month), 1)
    except ValueError:
        raise ValidationError("Invalid period. The period must be a valid year-month.")

    if value > get_last_month():
        raise ValidationError("Invalid period: year-month must be in the past.")


class MyTypes:
    PhoneNumber11 = partial(
        models.CharField,
        max_length=11,
        validators=[MinLengthValidator(10), PhoneNumber11_regex])

    PeriodYearMonth = partial(
        models.CharField,
        max_length=7,
        validators=[PeriodYearMonth_validate])

    PositiveMoneyField12 = partial(
        models.DecimalField,
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.0)])

