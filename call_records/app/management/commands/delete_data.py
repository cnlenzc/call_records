from django.core.management.base import BaseCommand
from app.models import StandingCharge, CallCharge, CallRecord, Bill


class Command(BaseCommand):
    help = 'Delete data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.delete_all(StandingCharge)
        self.delete_all(CallCharge)
        self.delete_all(CallRecord)
        self.delete_all(Bill)

    def delete_all(self, model):
        affected_rows = model.objects.all().delete()
        print('delete %s %s' % (model.__name__, affected_rows))
