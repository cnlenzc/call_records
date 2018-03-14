import json
from rest_framework.test import APITestCase


class APITestCase_myAssert(APITestCase):

    api_end_point = None

    def create(self, my_rec, doAssert):
        self.operation = 'create post'
        self.end_point = self.api_end_point
        response = self.client.post(self.end_point, data=my_rec['in'])
        if doAssert:
            self.myAssert(response, my_rec)
        return response.data.get('id', 0)

    def list(self, my_list, doAssert):
        self.operation = 'list get'
        self.end_point = self.api_end_point
        response = self.client.get(self.end_point)
        if doAssert:
            self.myAssert(response, my_list)

    def retrieve(self, my_rec, id, doAssert):
        self.operation = 'retrieve get'
        self.end_point = self.api_end_point + str(id) + '/'
        response = self.client.get(self.end_point)
        if doAssert:
            self.myAssert(response, my_rec)

    def destroy(self, my_rec, id, doAssert):
        self.operation = 'destroy delete'
        self.end_point = self.api_end_point + str(id) + '/'
        response = self.client.delete(self.end_point)
        if doAssert:
            self.myAssert(response, my_rec)

    def update(self, my_rec, id, doAssert):
        self.operation = 'update put'
        self.end_point = self.api_end_point + str(id) + '/'
        response = self.client.put(self.end_point, data=my_rec['in'])
        if doAssert:
            self.myAssert(response, my_rec)

    def partial_update(self, my_rec, id, doAssert):
        self.operation = 'partial_update patch'
        self.end_point = self.api_end_point + str(id) + '/'
        response = self.client.patch(self.end_point, data=my_rec['in'])
        if doAssert:
            self.myAssert(response, my_rec)

    def options(self, my_rec, doAssert):
        self.operation = 'options options'
        self.end_point = self.api_end_point
        response = self.client.options(self.end_point)
        if doAssert:
            self.myAssert(response, my_rec)

    def myAssert(self, response, my_rec):
        self.dump_msg = \
            '\n' \
            '*** CALL: %s %s\n' \
            '*** INPUT:\n' \
            '%s\n' \
            '*** OUTPUT: STATUS_CODE: %s EXPECTED: %s\n' \
            '%s\n' \
            '*** OUTPUT EXPECTED:\n' \
            '%s\n' \
            % (
                self.operation,
                self.end_point,
                json.dumps(my_rec.get('in', None), indent=4),
                getattr(response, "status_code", None),
                my_rec.get('status_code', None),
                json.dumps(getattr(response, "data", None), indent=4),
                json.dumps(my_rec.get("out", None), indent=4)
            )

        self.myAssertJson(response, my_rec)

    def __myAssertBaseType(self, response, expected, path):
        if response != expected:
            self.fail(
                "Field value does not match. "
                "path:'%s' response:'%s' expected:'%s' %s"
                % (path, response, expected, self.dump_msg))

    def __myAssertDict(self, response, expected, path):
        for key_dict in expected:
            new_path = '%s.%s' % (path, key_dict)
            if key_dict in response:
                self.__myAssertEqual(
                    response[key_dict], expected[key_dict], new_path)
            else:
                self.fail("Field not found. field:'%s' path:'%s' %s"
                          % (key_dict, path, self.dump_msg))

    def __myAssertList(self, response, expected, path):
        if len(response) != len(expected):
            self.fail(
                "List length does not match. "
                "path:'%s' response:'%s' expected:'%s' %s"
                % (path, len(response), len(expected), self.dump_msg))
        for i, item_expected in enumerate(expected):
            new_path = '%s[%s]' % (path, i)
            self.__myAssertEqual(response[i], expected[i], new_path)

    def __myAssertEqual(self, response, expected, path):
        # if isinstance(response, expected.__class__.__name__):
        if type(response) != type(expected) and \
           not (isinstance(expected, dict) and isinstance(response, dict)) and\
           not (isinstance(expected, list) and isinstance(response, list)) and\
           not (isinstance(expected, str) and isinstance(response, str)):
            self.fail(
                "Type mismatch. path:'%s' response:'%s' expected:'%s' %s"
                % (path, type(response), type(expected), self.dump_msg))

        if isinstance(expected, dict):
            self.__myAssertDict(response, expected, path)

        elif isinstance(expected, list):
            self.__myAssertList(response, expected, path)

        elif isinstance(expected, (str, bool, int, float, type(None))):
            self.__myAssertBaseType(response, expected, path)

        else:
            self.fail("This type is not allowed. "
                      "path:'%s' response:'%s' expected:'%s' %s"
                      % (path, type(response), type(expected), self.dump_msg))

    def myAssertJson(self, response, expected, path='json'):
        if 'status_code' in expected:
            if response.status_code != expected['status_code']:
                self.fail(
                    "STATUS_CODE does not match. "
                    "path:'%s' response:'%s' expected:'%s' %s"
                    % (path, response.status_code,
                       expected['status_code'], self.dump_msg))
        else:
            self.fail("The 'status_code' field is not on the expected record")

        if 'out' in expected:
            self.__myAssertEqual(getattr(response, "data", None),
                                 expected['out'], path)
        else:
            self.fail("The 'out' field is not on the expected record")
