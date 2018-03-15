"""
Improve Assert for Json API
"""
import json
from rest_framework.test import APITestCase


class APITestCase_myAssert(APITestCase):
    """
    Class to improve APITest to simplify automatic testing
    """

    api_end_point = None

    def create(self, my_rec, doAssert):
        """
        Call and assert create
        :param my_rec:
        :param doAssert:
        :return:
        """
        self.operation = 'create post'
        self.end_point = self.api_end_point
        response = self.client.post(self.end_point, data=my_rec['in'])
        if doAssert:
            self.myAssert(response, my_rec)
        return response.data.get('id', 0)

    def list(self, my_list, doAssert):
        """
        call and assert list
        :param my_list:
        :param doAssert:
        :return:
        """
        self.operation = 'list get'
        self.end_point = self.api_end_point
        response = self.client.get(self.end_point)
        if doAssert:
            self.myAssert(response, my_list)

    def retrieve(self, my_rec, pk, doAssert):
        """
        call and assert retrieve
        :param my_rec:
        :param pk:
        :param doAssert:
        :return:
        """
        self.operation = 'retrieve get'
        self.end_point = self.api_end_point + str(pk) + '/'
        response = self.client.get(self.end_point)
        if doAssert:
            self.myAssert(response, my_rec)

    def destroy(self, my_rec, pk, doAssert):
        """
        call and assert destroy
        :param my_rec:
        :param pk:
        :param doAssert:
        :return:
        """
        self.operation = 'destroy delete'
        self.end_point = self.api_end_point + str(pk) + '/'
        response = self.client.delete(self.end_point)
        if doAssert:
            self.myAssert(response, my_rec)

    def update(self, my_rec, pk, doAssert):
        """
        call and assert update
        :param my_rec:
        :param pk:
        :param doAssert:
        :return:
        """
        self.operation = 'update put'
        self.end_point = self.api_end_point + str(pk) + '/'
        response = self.client.put(self.end_point, data=my_rec['in'])
        if doAssert:
            self.myAssert(response, my_rec)

    def partial_update(self, my_rec, pk, doAssert):
        """
        call and assert partial_update
        :param my_rec:
        :param pk:
        :param doAssert:
        :return:
        """
        self.operation = 'partial_update patch'
        self.end_point = self.api_end_point + str(pk) + '/'
        response = self.client.patch(self.end_point, data=my_rec['in'])
        if doAssert:
            self.myAssert(response, my_rec)

    def options(self, my_rec, doAssert):
        """
        call and assert options
        :param my_rec:
        :param doAssert:
        :return:
        """
        self.operation = 'options options'
        self.end_point = self.api_end_point
        response = self.client.options(self.end_point)
        if doAssert:
            self.myAssert(response, my_rec)

    def myAssert(self, response, my_rec):
        """
        assert json API and prepare to print dump for fails
        :param response:
        :param my_rec:
        :return:
        """
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
        """
        assert base types like str, int, float, None
        :param response:
        :param expected:
        :param path:
        :return:
        """
        if response != expected:
            self.fail(
                "Field value does not match. "
                "path:'%s' response:'%s' expected:'%s' %s"
                % (path, response, expected, self.dump_msg))

    def __myAssertDict(self, response, expected, path):
        """
        assert the dict and its descendants
        :param response:
        :param expected:
        :param path:
        :return:
        """
        for key_dict in expected:
            new_path = '%s.%s' % (path, key_dict)
            if key_dict in response:
                self.__myAssertEqual(
                    response[key_dict], expected[key_dict], new_path)
            else:
                self.fail("Field not found. field:'%s' path:'%s' %s"
                          % (key_dict, path, self.dump_msg))

    def __myAssertList(self, response, expected, path):
        """
        assert the list and its descendants
        :param response:
        :param expected:
        :param path:
        :return:
        """
        if len(response) != len(expected):
            self.fail(
                "List length does not match. "
                "path:'%s' response:'%s' expected:'%s' %s"
                % (path, len(response), len(expected), self.dump_msg))
        for i, item_expected in enumerate(expected):
            new_path = '%s[%s]' % (path, i)
            self.__myAssertEqual(response[i], item_expected, new_path)

    def __myAssertEqual(self, response, expected, path):
        """
        checks the type and calls a specific method
        :param response:
        :param expected:
        :param path:
        :return:
        """
        if isinstance(expected, dict):
            self.__check_type_mismatch(response, expected, path, dict)
            self.__myAssertDict(response, expected, path)

        elif isinstance(expected, list):
            self.__check_type_mismatch(response, expected, path, list)
            self.__myAssertList(response, expected, path)

        elif isinstance(expected, str):
            self.__check_type_mismatch(response, expected, path, str)
            self.__myAssertBaseType(response, expected, path)

        elif isinstance(expected, bool):
            self.__check_type_mismatch(response, expected, path, bool)
            self.__myAssertBaseType(response, expected, path)

        elif isinstance(expected, int):
            self.__check_type_mismatch(response, expected, path, int)
            self.__myAssertBaseType(response, expected, path)

        elif isinstance(expected, float):
            self.__check_type_mismatch(response, expected, path, float)
            self.__myAssertBaseType(response, expected, path)

        elif isinstance(expected, type(None)):
            self.__check_type_mismatch(response, expected, path, type(None))
            self.__myAssertBaseType(response, expected, path)

        else:
            self.fail("This type is not allowed. "
                      "path:'%s' response:'%s' expected:'%s' %s"
                      % (path, type(response), type(expected), self.dump_msg))

    def __check_type_mismatch(self, response, expected, path, item_type):
        """
        check the type
        :param response:
        :param expected:
        :param path:
        :param item_type:
        :return:
        """
        if not isinstance(response, item_type):
            self.fail(
                "Type mismatch. path:'%s' response:'%s' expected:'%s' %s"
                % (path, type(response), type(expected), self.dump_msg))

    def myAssertJson(self, response, expected, path='json'):
        """
        assert json API
        :param response:
        :param expected:
        :param path:
        :return:
        """
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
