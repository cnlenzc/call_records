from app.tests.my_assert import APITestCase_myAssert
from .data_retrieve import Records_retrieve as recd
from . import API_END_POINT


class RetrieveAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_retrieve_ok(self):
        id1 = self.create(recd.ok1['create'], doAssert=False)
        self.retrieve(recd.ok1, id1, doAssert=True)
