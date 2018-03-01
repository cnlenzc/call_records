from app.tests.my_assert import APITestCase_myAssert
from .data_create import Records_create as rec
from . import API_END_POINT


class CallRecord_CreateAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_create_ok(self):
        self.create(rec.ok1, doAssert=True)
        self.create(rec.ok2, doAssert=True)

    def test_create_null(self):
        self.create(rec.all_null, doAssert=True)

    def test_invalid_price(self):
        self.create(rec.invalid_price, doAssert=True)

    def test_invalid_price2(self):
        self.create(rec.invalid_price2, doAssert=True)

