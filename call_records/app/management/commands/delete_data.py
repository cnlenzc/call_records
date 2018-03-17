"""
Command to delete all data
"""
from django.core.management.base import BaseCommand
from app.models import ConfigPrice, CallRecord, Bill


class Command(BaseCommand):
    """ Command to delete all data """
    help = 'Delete data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        delete_all(ConfigPrice)
        delete_all(CallRecord)
        delete_all(Bill)


def delete_all(model):
    """ delete and print results """
    affected_rows = model.objects.all().delete()
    print('delete %s %s' % (model.__name__, affected_rows))
