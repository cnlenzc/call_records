"""
automatic test for this operation
"""
from app.tests.my_assert import APITestCase_myAssert
from .data_partial_update import Records_partial_update as rec
from . import API_END_POINT


class PartialUpdateAPI(APITestCase_myAssert):
    """
    test cases for this operation
    """

    api_end_point = API_END_POINT

    def test_partial_update_ok(self):
        """ test operation update ok """
        pk = self.create(rec.ok1['create'], doAssert=False)
        self.partial_update(rec.ok1, pk, doAssert=True)

    def test_partial_update_not_found(self):
        """ test operation update not found """
        self.partial_update(rec.not_found, 1, doAssert=True)
        id1 = self.create(rec.not_found['create'], doAssert=False)
        self.partial_update(rec.not_found, id1 + 1, doAssert=True)

    def test_partial_update_not_unique(self):
        """ create update not unique """
        for my_rec in rec.not_unique['create']:
            pk = self.create(my_rec, doAssert=False)

        self.partial_update(rec.not_unique, pk, doAssert=True)
