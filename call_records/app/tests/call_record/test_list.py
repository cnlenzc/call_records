"""
automatic test for this operation
"""
from app.tests.my_assert import APITestCase_myAssert
from .data_list import Records_list as rec
from . import API_END_POINT


class ListAPI(APITestCase_myAssert):
    """
    test cases for this operation
    """

    api_end_point = API_END_POINT

    def test_list_ok(self):
        """ list all calls """
        for my_rec in rec.list_ok['create']:
            self.create(my_rec, doAssert=False)
        self.list(rec.list_ok, doAssert=True)

    def test_list_empty(self):
        """ empty list """
        self.list(rec.list_empty, doAssert=True)
