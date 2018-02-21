from rest_framework.test import APITestCase
from rest_framework import status
from .data import \
    rec1, rec2

API_END_POINT = '/call-record/'

class CreateAPI(APITestCase):

    def test_create_ok(self):
        response1 = self.client.post(API_END_POINT, data=rec1['in'])
        self.myAssertCreate(response1, rec1)

        response2 = self.client.post(API_END_POINT, data=rec2['in'])
        self.myAssertCreate(response2, rec2)

    def myAssertCreate(self, response, rec):
        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            rec_out = rec['out']
            for item in rec_out:
                str_res = '%s:%s' % (item, response.data[item])
                str_out = '%s:%s' % (item, rec_out[item])
                self.assertEqual(str_res, str_out)
        except AssertionError as err:
            print('** ERROR in the return of create operation')
            print('** input: %s' % rec['in'])
            print('** status_code: %s' % response.status_code)
            print('** output: %s' % response.data)
            raise err
