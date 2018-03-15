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

    def test_update_not_found(self):
        """ test operation update not found """
        self.update(rec.not_found, 1, doAssert=True)
        id1 = self.create(rec.not_found['create'], doAssert=False)
        self.update(rec.not_found, id1 + 1, doAssert=True)

    def test_update_not_unique(self):
        """ create update not unique """
        for my_rec in rec.not_unique['create']:
            pk = self.create(my_rec, doAssert=False)
        self.update(rec.not_unique, pk, doAssert=True)
