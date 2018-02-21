from django.db import models
from django.core.validators import RegexValidator

START = '1'
END = '2'
choices_type = ((START, 'start'), (END, 'end'))

phone_regex = RegexValidator(
    regex = r'^\d{10,11}$',
    message = "Phone number must be entered in the format: 'AAXXXXXXXXX'. "
              "Where AA is the area code and XXXXXXXXX is the phone number.")


class CallRecord(models.Model):
    type = models.CharField(
        help_text = "Indicate if it's a call 'start' or 'end' record",
        max_length = 1,
        choices = choices_type)

    timestamp = models.PositiveIntegerField(
        help_text = "The timestamp of when the event occured")

    call_id = models.PositiveIntegerField(
        help_text = "Unique for each call record pair")

    source = models.CharField(
        help_text = "The subscriber phone number that originated the call",
        max_length = 11,
        null = True,
        validators = [phone_regex])

    destination = models.CharField(
        help_text = "The subscriber phone number that originated the call",
        max_length = 11,
        null = True,
        validators = [phone_regex])

    class Meta:
        indexes = [
            models.Index(
                fields=['call_id', 'type'],
                name='call_id_type_idx'),
            models.Index(
                fields=['call_id', 'timestamp', 'type'],
                name='call_id_timestamp_type_idx'),
            models.Index(
                fields=['source', 'timestamp'],
                name='source_timestamp_idx'),
        ]
        unique_together = ('call_id', 'type')
        ordering = ('call_id', 'timestamp', 'type')

    def __str__(self):
        return '%s %s source:%s timestamp:%s' % \
               (self.type, self.call_id, self.source, self.timestamp)


