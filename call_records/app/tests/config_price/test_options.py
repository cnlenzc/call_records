"""
automatic test for this operation
"""
from app.tests.my_assert import APITestCase_myAssert
from .data_options import Records_options as rec
from . import API_END_POINT


class OptionsAPI(APITestCase_myAssert):
    """
    test cases for this operation
    """

    api_end_point = API_END_POINT

    def test_options_ok(self):
        """ test operation option """
        self.options(rec.ok, doAssert=True)
