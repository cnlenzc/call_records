from app.tests.my_assert import APITestCase_myAssert
from .data_partial_update import Records_partial_update as rec
from . import API_END_POINT


class CallRecord_PartialUpdateAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_partial_update_ok(self):
        id = self.create(rec.ok1['create'], doAssert=False)
        self.partial_update(rec.ok1, id, doAssert=True)


