"""
automatic test for this operation
"""
from app.tests.my_assert import APITestCase_myAssert
from .data_create import Records_create as rec
from . import API_END_POINT


class CreateAPI(APITestCase_myAssert):
    """
    test cases for this operation
    """

    api_end_point = API_END_POINT

    def test_create_ok(self):
        """ test case to create a call ok """
        self.create(rec.ok1, doAssert=True)
        self.create(rec.ok2, doAssert=True)

    def test_create_not_unique(self):
        """ create the same call twice, in the second you get an error """
        self.create(rec.ok1, doAssert=True)
        self.create(rec.not_unique, doAssert=True)

    def test_create_blank(self):
        """ try to create call with all the fields blank """
        self.create(rec.all_blank, doAssert=True)

    def test_create_null(self):
        """ try to create call with all the fields null """
        self.create(rec.all_null, doAssert=True)

    def test_start_without_source_destination(self):
        """ try to create call without source and destination """
        self.create(rec.start_without_source_destination, doAssert=True)

    def test_invalid_phone_number1(self):
        """ try to create call with invalid phone number """
        self.create(rec.invalid_phone_number1, doAssert=True)

    def test_invalid_phone_number2(self):
        """ try to create call with invalid phone number """
        self.create(rec.invalid_phone_number2, doAssert=True)

    def test_invalid_type(self):
        """ try to create call with invalid type """
        self.create(rec.invalid_type, doAssert=True)

    def test_invalid_timestamp_and_call_id1(self):
        """ try to create call with invalid timestamp and call_id """
        self.create(rec.invalid_timestamp_and_call_id1, doAssert=True)

    def test_invalid_timestamp_and_call_id2(self):
        """ try to create call with invalid timestamp and call_id """
        self.create(rec.invalid_timestamp_and_call_id2, doAssert=True)
