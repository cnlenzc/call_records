from app.tests.my_assert import APITestCase_myAssert
from .data_destroy import Records_destroy as recd
from . import API_END_POINT


class CallRecord_DestroyAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_destroy_ok(self):
        id1 = self.create(recd.ok1['create'], doAssert=False)
        id2 = self.create(recd.ok2['create'], doAssert=True)
        self.destroy(recd.ok1, id1, doAssert=True)
        self.destroy(recd.ok2, id2, doAssert=True)

    def test_destroy_not_found(self):
        self.destroy(recd.not_found, 1, doAssert=True)
        id1 = self.create(recd.ok1['create'], doAssert=False)
        self.destroy(recd.not_found, id1 + 1, doAssert=True)
