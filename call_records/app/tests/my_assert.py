import json
from rest_framework.test import APITestCase


class APITestCase_myAssert(APITestCase):

    api_end_point = None

    def create(self, my_rec, doAssert):
        response = self.client.post(self.api_end_point, data=my_rec['in'])
        if doAssert:
            self.myAssert(response, my_rec)
        return response.data.get('id', 0)

    def list(self, my_list, doAssert):
        response = self.client.get(self.api_end_point)
        if doAssert:
            self.myAssert(response, my_list)

    def retrieve(self, my_rec, id, doAssert):
        resp = self.client.get(self.api_end_point + str(id) + '/')
        if doAssert:
            self.myAssert(resp, my_rec, id)

    def destroy(self, my_rec, id, doAssert):
        resp = self.client.delete(self.api_end_point + str(id) + '/')
        if doAssert:
            self.myAssert(resp, my_rec, id)

    def update(self, my_rec, id, doAssert):
        resp = self.client.put(self.api_end_point + str(id) + '/', data=my_rec['in'])
        if doAssert:
            self.myAssert(resp, my_rec, id)

    def partial_update(self, my_rec, id, doAssert):
        resp = self.client.patch(self.api_end_point + str(id) + '/', data=my_rec['in'])
        if doAssert:
            self.myAssert(resp, my_rec, id)

    def options(self, my_rec, doAssert):
        resp = self.client.options(self.api_end_point)
        if doAssert:
            self.myAssert(resp, my_rec)

    def myAssert(self, response, my_rec, id=None):
        try:
            self.myAssertJson(response, my_rec)

        except AssertionError as err:
            print()
            print('**** ERROR in the return of API')
            print('*** INPUT: id: %s' % id)
            print(json.dumps(my_rec.get('in', {}), indent=4))
            print('*** OUTPUT: STATUS_CODE: %s EXPECTED: %s' %
                  (response.status_code, my_rec.get('status_code', None)))
            print(json.dumps(getattr(response, "data", {}), indent=4))
            print('*** OUTPUT EXPECTED:')
            print(json.dumps(my_rec.get("out", {}), indent=4))
            raise err

    def __myAssertBaseType(self, response, expected, path):
        if response != expected:
            self.fail(
                "Different value in json. field:'%s' response:'%s' expected:'%s'"
                % (path, response, expected))

    def __myAssertDict(self, response, expected, path):
        for key_dict in expected:
            new_path = '%s.%s' % (path, key_dict)
            if key_dict in response:
                self.__myAssertEqual(response[key_dict], expected[key_dict], new_path)
            else:
                self.fail("The '%s' field not found in json. path:'%s'"
                    % (key_dict, path))

    def __myAssertList(self, response, expected, path):
        if len(response) != len(expected):
            self.fail(
                "Different list length in Json. path:'%s' response:'%s' expected:'%s'"
                % (path, len(response), len(expected)))
        for i, item_expected in enumerate(expected):
            new_path = '%s[%s]' % (path, i)
            self.__myAssertEqual(response[i], expected[i], new_path)

    def __myAssertEqual(self, response, expected, path):
        # if isinstance(response, expected.__class__):
        if type(response) != type(expected) and \
                not (isinstance(expected, dict) and isinstance(response, dict)) and \
                not (isinstance(expected, list) and isinstance(response, list)) and \
                not (isinstance(expected, str) and isinstance(response, str)):
            self.fail(
                "Type mismatch on Json. path:'%s' response:'%s' expected:'%s'"
                % (path, type(response), type(expected)))

        if isinstance(expected, dict):
            self.__myAssertDict(response, expected, path)

        elif isinstance(expected, list):
            self.__myAssertList(response, expected, path)

        elif isinstance(expected, (str, bool, int, type(None))):
            self.__myAssertBaseType(response, expected, path)

        else:
            self.fail("Type '%s' in '%s' is not allowed" % (type(expected), path))

    def myAssertJson(self, response, expected, path='json'):
        if 'status_code' in expected:
            if response.status_code != expected['status_code']:
                self.fail(
                    "Different status_code in json. path:'%s' response:'%s' expected:'%s'"
                    % (path, response.status_code, expected['status_code']))
        else:
            self.fail("The 'status_code' field is not on the expected record")

        if 'out' in expected:
            self.__myAssertEqual(response.data, expected['out'], path)
        else:
            self.fail("The 'out' field is not on the expected record")

