from app.tests.my_assert import APITestCase_myAssert
from .data_update import Records_update as rec
from . import API_END_POINT


class CallRecord_UpdateAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_update_ok(self):
        id1 = self.create(rec.ok1['create'], doAssert=False)
        self.update(rec.ok1, id1, doAssert=True)

    def test_update_not_found(self):
        self.update(rec.not_found, 1, doAssert=True)
        id1 = self.create(rec.not_found['create'], doAssert=False)
        self.update(rec.not_found, id1 + 1, doAssert=True)

    def test_update_not_unique(self):
        for my_rec in rec.not_unique['create']:
            id = self.create(my_rec, doAssert=False)
        self.update(rec.not_unique, id, doAssert=True)
