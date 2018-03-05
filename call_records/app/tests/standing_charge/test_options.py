from app.tests.my_assert import APITestCase_myAssert
from .data_options import Records_options as rec
from . import API_END_POINT


class OptionsAPI(APITestCase_myAssert):

    api_end_point = API_END_POINT

    def test_options_ok(self):
        self.options(rec.ok, doAssert=True)

