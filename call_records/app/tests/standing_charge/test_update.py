"""
automatic test for this operation
"""
from app.tests.my_assert import APITestCase_myAssert
from .data_update import Records_update as rec
from . import API_END_POINT


class UpdateAPI(APITestCase_myAssert):
    """
    test cases for this operation
    """

    api_end_point = API_END_POINT

    def test_update_ok(self):
        """ test operation update ok """
        id1 = self.create(rec.ok1['create'], doAssert=False)
        self.update(rec.ok1, id1, doAssert=True)
