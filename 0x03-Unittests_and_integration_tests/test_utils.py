#!/usr/bin/env python3
"""Module function that inherits from unittest.TestCase"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    This class uses parameterized.expand to allow
    multiple sets of inputs and their corresponding
    expected results
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with various inputs.

        Parameters:
            - nested_map: A nested map.
            - path: A sequence of keys representing a path to the value.
            - expected_result: The expected result when accessing the
            nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

        @parameterized.expand([
            ({}, ("a",), KeyError, "Key not found: 'a'"),
            ({"a": 1}, ("a", "b"), KeyError, "Key not found: 'b'"),
        ])
        def test_access_nested_map_exception(
                self, nested_map, path, expected_exception, expected_message):
            """
            Test that accessing nested_map with certain inputs
            raises a KeyError with the expected message.

            Parameters:
                - nested_map: A nested map.
                - path: A sequence of keys representing a path to the value.
                - expected_exception: The expected exception class.
                - expected_message: The expected exception message.
            """
            with self.assertRaises(expected_exception) as context:
                access_nested_map(nested_map, path)

            self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """
    class TestGetJson that checks that the output of get_json
    is equal to the test_payload.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that utils.get_json returns the expected result using mocked
        HTTP calls

        Parameters:
            - test_url: The URL to test.
            - test_payload: The expected JSON payload.
        """
        # Mock the response of requests.get
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assert that the mocked get method was called exactly once 
        # with test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)
