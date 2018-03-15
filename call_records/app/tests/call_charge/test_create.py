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
        """ test case to create ok """
        self.create(rec.ok1, doAssert=True)
        self.create(rec.ok2, doAssert=True)

    def test_create_null(self):
        """ try to create with all the fields blank """
        self.create(rec.all_null, doAssert=True)

    def test_invalid_price(self):
        """ try to create with all the fields null """
        self.create(rec.invalid_price, doAssert=True)
