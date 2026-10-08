"""Recursive JSON key search with field-level role-based access control."""

try:
	from .policy import POLICY
except ImportError:
	from policy import POLICY


def json_search(key, input_object, role=None):
	"""Return all values for ``key`` that the caller's role may read."""
	caller_role = "viewer" if role is None else role
	allowed_roles = POLICY.get(key)
	if allowed_roles is None or caller_role not in allowed_roles:
		return []

	results = []

	def search(value):
		if isinstance(value, dict):
			for current_key, current_value in value.items():
				if current_key == key:
					results.append(current_value)
				search(current_value)
		elif isinstance(value, list):
			for item in value:
				search(item)

	search(input_object)
	return results
