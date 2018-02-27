from app.tests.my_assert import APITestCase_myAssert
from .data_create import Records_create as rec
from . import API_END_POINT


class CallRecord_CreateAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_create_ok(self):
        self.create(rec.ok1, doAssert=True)
        self.create(rec.ok2, doAssert=True)

    def test_create_not_unique(self):
        self.create(rec.ok1, doAssert=True)
        self.create(rec.not_unique, doAssert=True)

    def test_create_blank(self):
        self.create(rec.all_blank, doAssert=True)

    def test_create_null(self):
        self.create(rec.all_null, doAssert=True)

    def test_start_without_source_destination(self):
        self.create(rec.start_without_source_destination, doAssert=True)

    def test_invalid_phone_number1(self):
        self.create(rec.invalid_phone_number1, doAssert=True)

    def test_invalid_phone_number2(self):
        self.create(rec.invalid_phone_number2, doAssert=True)

    def test_invalid_type(self):
        self.create(rec.invalid_type, doAssert=True)

    def test_invalid_timestamp_and_id1(self):
        self.create(rec.invalid_timestamp_and_call_id1, doAssert=True)

    def test_invalid_timestamp_and_id2(self):
        self.create(rec.invalid_timestamp_and_call_id2, doAssert=True)

