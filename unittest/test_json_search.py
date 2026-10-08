import unittest
from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    '''test module to test search function in `recursive_json_search.py`'''

    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

# --- Security Test Cases bổ sung ---
    def test_get_apikey_as_viewer(self):
        '''Viewer không được phép đọc apiKey (trả về list rỗng)'''
        self.assertEqual([], json_search("apiKey", data, role="viewer"))

    def test_get_apikey_as_admin(self):
        '''Admin được phép đọc apiKey (trả về danh sách chứa apiKey)'''
        self.assertNotEqual([], json_search("apiKey", data, role="admin"))

    def test_get_apikey_without_role(self):
        '''Không truyền role (mặc định viewer) không được phép đọc apiKey'''
        self.assertEqual([], json_search("apiKey", data))

    def test_viewer_cannot_read_management_ip(self):
        '''Viewer không được phép đọc managementIpAddress'''
        self.assertEqual([], json_search("managementIpAddress", data, role="viewer"))

    def test_operator_can_read_management_ip(self):
        '''Operator được phép đọc managementIpAddress'''
        self.assertNotEqual([], json_search("managementIpAddress", data, role="operator"))


if __name__ == '__main__':
    unittest.main()
