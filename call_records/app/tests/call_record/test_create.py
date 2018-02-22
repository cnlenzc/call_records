from app.tests.my_assert import APITestCase_myAssert
from .data import Records


class CreateAPI(APITestCase_myAssert):

    API_END_POINT = '/call-record/'

    def test_create_ok(self):
        self.call_post_and_assert(Records.ok1)
        self.call_post_and_assert(Records.ok2)

    def test_create_not_unique(self):
        self.call_post_and_assert(Records.ok1)
        self.call_post_and_assert(Records.not_unique)

    def test_create_blank(self):
        self.call_post_and_assert(Records.all_blank)

    def test_create_null(self):
        self.call_post_and_assert(Records.all_null)

    def test_start_without_source_destination(self):
        self.call_post_and_assert(Records.start_without_source_destination)

    def test_invalid_phone_number1(self):
        self.call_post_and_assert(Records.invalid_phone_number1)

    def test_invalid_phone_number2(self):
        self.call_post_and_assert(Records.invalid_phone_number2)

    def test_invalid_type(self):
        self.call_post_and_assert(Records.invalid_type)

    def test_invalid_timestamp_and_call_id1(self):
        self.call_post_and_assert(Records.invalid_timestamp_and_call_id1)

    def test_invalid_timestamp_and_call_id2(self):
        self.call_post_and_assert(Records.invalid_timestamp_and_call_id2)

