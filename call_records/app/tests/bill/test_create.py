"""
automatic test for this operation
"""
from django.core.management import call_command
from app.tests.my_assert import APITestCase_myAssert
from .data_create import Records_create as rec
from . import API_END_POINT


class CreateAPI(APITestCase_myAssert):
    """
    test cases for this operation
    """

    api_end_point = API_END_POINT

    @classmethod
    def setUpTestData(cls):
        """ Set up data for the whole TestCase """
        call_command('create_data')

    def test_create_ok_no_calls(self):
        """ test case to create bill with no calls """
        self.create(rec.ok_no_calls, doAssert=True)

    def test_create_ok_no_calls_and_default_period(self):
        """ test case to create bill wihout no period """
        self.create(rec.ok_no_calls_and_default_period, doAssert=True)

    def test_create_ok_1_call(self):
        """ test case to create bill with 1 call """
        self.create(rec.ok_1_call, doAssert=True)

    def test_create_ok_end_of_call_out_of_period(self):
        """ one of calls start at period and end in the next """
        self.create(rec.ok_end_of_call_out_of_period, doAssert=True)

    def test_create_ok_5_calls(self):
        """ test case to create bill with 5 calls """
        self.create(rec.ok_5_calls, doAssert=True)

    def test_create_ok_near_60seg(self):
        """ test case to create bill with 59seg, 60seg and 61seg """
        self.create(rec.ok_near_60seg, doAssert=True)

    def test_create_not_unique(self):
        """ create the same bill twice,
            in the second only retrieve the bill """
        self.create(rec.ok_no_calls, doAssert=True)
        self.create(rec.not_unique, doAssert=True)

    def test_create_blank(self):
        """ try to create bill with all the fields blank """
        self.create(rec.all_blank, doAssert=True)

    def test_create_null(self):
        """ try to create bill with all the fields null """
        self.create(rec.all_null, doAssert=True)

    def test_invalid_phone_number1(self):
        """ try to create bill with invalid phone number """
        self.create(rec.invalid_phone_number1, doAssert=True)

    def test_invalid_phone_number2(self):
        """ try to create bill with invalid phone number """
        self.create(rec.invalid_phone_number2, doAssert=True)

    def test_invalid_period_date(self):
        """ try to create bill with invalid period date """
        self.create(rec.invalid_period_date, doAssert=True)

    def test_invalid_period_format(self):
        """ try to create bill with invalid period format """
        self.create(rec.invalid_period_format, doAssert=True)

    def test_invalid_period_future(self):
        """ try to create bill with period in future """
        self.create(rec.invalid_period_future, doAssert=True)
