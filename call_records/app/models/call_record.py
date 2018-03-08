from django.db import models
from util import MyTypes


START = '1'
END = '2'
choices_type = ((START, 'start'), (END, 'end'))


class CallRecord(models.Model):
    type = models.CharField(
        help_text = "Indicate if it's a call 'start' or 'end' record",
        max_length = 1,
        choices = choices_type)

    timestamp = models.PositiveIntegerField(
        help_text = "The timestamp of when the event occured")

    call_id = models.PositiveIntegerField(
        help_text = "Unique for each call record pair")

    source = MyTypes.PhoneNumber11(
        help_text = "The subscriber phone number that originated the call",
        null = True)

    destination = MyTypes.PhoneNumber11(
        help_text = "The phone number receiving the call",
        null = True)

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


