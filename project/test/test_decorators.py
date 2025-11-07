import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from revision.hw_functions_utils import wrap_in_dict

@wrap_in_dict
def test_function_str(name):
    return f"Hello, {name}"

@wrap_in_dict
def test_function_int(a, b):
    return a * b

class TestDecorator(unittest.TestCase):

    def test_return_type_is_dict(self):
        result = test_function_str("Test")
        self.assertIsInstance(result, dict)

    def test_string_function_result(self):
        expected = {"result": "Hello, World"}
        actual = test_function_str("World")
        self.assertEqual(actual, expected)

    def test_integer_function_result(self):
        expected = {"result": 50}
        actual = test_function_int(10, 5)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()