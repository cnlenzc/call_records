from app.tests.my_assert import APITestCase_myAssert
from .data_list import Records_list as rec
from . import API_END_POINT


class CallRecord_ListAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_list_ok(self):
        for my_rec in rec.list_ok['create']:
            self.create(my_rec, doAssert=False)
        self.list(rec.list_ok, doAssert=True)

    def test_list_empty(self):
        self.list(rec.list_empty, doAssert=True)
