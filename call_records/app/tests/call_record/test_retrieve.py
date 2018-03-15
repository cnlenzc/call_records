"""
automatic test for this operation
"""
from app.tests.my_assert import APITestCase_myAssert
from .data_retrieve import Records_retrieve as recd
from . import API_END_POINT


class RetrieveAPI(APITestCase_myAssert):
    """
    test cases for this operation
    """

    api_end_point = API_END_POINT

    def test_retrieve_ok(self):
        """ test operation retrieve ok """
        id1 = self.create(recd.ok1['create'], doAssert=False)
        self.retrieve(recd.ok1, id1, doAssert=True)
        id2 = self.create(recd.ok2['create'], doAssert=False)
        self.retrieve(recd.ok2, id2, doAssert=True)

    def test_retrieve_not_found(self):
        """ test operation retrieve not found """
        self.retrieve(recd.not_found, 1, doAssert=True)
        id1 = self.create(recd.ok1['create'], doAssert=False)
        self.retrieve(recd.not_found, id1 + 1, doAssert=True)
