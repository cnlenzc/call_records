from django.core.management import call_command
from app.tests.my_assert import APITestCase_myAssert
from .data_create import Records_create as rec
from . import API_END_POINT


class CreateAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        call_command('create_data')

    def test_create_ok_no_calls(self):
        self.create(rec.ok1, doAssert=True)
        self.create(rec.ok2, doAssert=True)

    def test_create_ok_1_call(self):
        self.create(rec.ok_1_call, doAssert=True)

    def test_create_ok_2_calls(self):
        self.create(rec.ok_2_calls, doAssert=True)

    def test_create_ok_5_calls(self):
        self.create(rec.ok_5_calls, doAssert=True)

    def test_create_ok_near_60seg(self):
        self.create(rec.ok_near_60seg, doAssert=True)

    def test_create_not_unique(self):
        self.create(rec.ok2, doAssert=True)
        self.create(rec.not_unique, doAssert=True)

    def test_create_blank(self):
        self.create(rec.all_blank, doAssert=True)

    def test_create_null(self):
        self.create(rec.all_null, doAssert=True)

    def test_invalid_phone_number1(self):
        self.create(rec.invalid_phone_number1, doAssert=True)

    def test_invalid_phone_number2(self):
        self.create(rec.invalid_phone_number2, doAssert=True)

    def test_invalid_period_date(self):
        self.create(rec.invalid_period_date, doAssert=True)

    def test_invalid_period_format(self):
        self.create(rec.invalid_period_format, doAssert=True)

    def test_invalid_period_future(self):
        self.create(rec.invalid_period_future, doAssert=True)

