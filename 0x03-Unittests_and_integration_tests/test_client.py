#!/usr/bin/env python3
"""Module function that inherits from unittest.TestCase"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"repos_url": "dummy_url"})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Parameters:
            - org_name: The organization name.
        """
        client = GithubOrgClient(org_name)

        # Access org property
        result = client.org

        # Assert that get_json is called once with the expected args
        mock_get_json.assert_called_once_with(client.ORG_URL.format(
            org=org_name))

        # Assert that the result is a dictionary
        self.assertIsInstance(result, dict)
