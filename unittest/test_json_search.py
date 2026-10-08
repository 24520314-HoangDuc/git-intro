import unittest

try:
	from .recursive_json_search import json_search
	from .test_data import data, key1, key2
except ImportError:
	from recursive_json_search import json_search
	from test_data import data, key1, key2


class json_search_test(unittest.TestCase):
	def test_search_found(self):
		"""Find every occurrence of a permitted key in nested objects."""
		result = json_search(key1, data)

		self.assertEqual(len(result), 1)
		self.assertEqual(result[0], "Network Device 10.10.20.82 Is Unreachable From Controller")

	def test_search_not_found(self):
		"""Return an empty list when the requested key is absent."""
		self.assertEqual(json_search(key2, data), [])

	def test_is_a_list(self):
		"""Always return a list for a successful search."""
		self.assertIsInstance(json_search(key1, data), list)

	def test_api_key_requires_admin(self):
		"""Deny API key values to the default viewer role."""
		self.assertEqual(json_search("apiKey", data), [])

	def test_api_key_allows_admin(self):
		"""Allow API key values to administrators."""
		self.assertEqual(json_search("apiKey", data, role="admin"), ["SNMP-COMMUNITY-STRING-7f3a9c"])

	def test_management_ip_requires_operator_or_admin(self):
		"""Deny management IP values to viewers."""
		self.assertEqual(json_search("managementIpAddress", data, role="viewer"), [])

	def test_management_ip_allows_operator(self):
		"""Allow management IP values to operators."""
		self.assertEqual(json_search("managementIpAddress", data, role="operator"), ["10.10.20.21"])


if __name__ == "__main__":
	unittest.main()
