import json
from rest_framework.test import APITestCase


class APITestCase_myAssert(APITestCase):

    API_END_POINT = None

    def call_post_and_assert(self, my_rec):
        resp = self.client.post(self.API_END_POINT, data=my_rec['in'])
        self.myAssert(resp, my_rec)

    def myAssert(self, response, my_rec):
        try:
            self.assertEqual(response.status_code, my_rec['status_code'])
            rec_out = my_rec['out']
            for item in rec_out:
                str_res = '%s: %s' % (item, response.data.get(item, 'null'))
                str_out = '%s: %s' % (item, rec_out.get(item, 'null'))
                self.assertEqual(str_res, str_out)

        except AssertionError as err:
            print()
            print('**** ERROR in the return of operation')
            print('*** INPUT:')
            print(json.dumps(my_rec['in'], indent=4))
            print('*** OUTPUT: STATUS_CODE: %s EXPECTED: %s' %
                  (response.status_code, my_rec['status_code']))
            print(json.dumps(getattr(response,"data", {}), indent=4))
            raise err
