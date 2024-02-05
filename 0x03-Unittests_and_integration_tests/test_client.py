#!/usr/bin/env python3
"""Module function that inherits from unittest.TestCase"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test the GithubOrgClient._public_repos_url property.

        This method mocks the GithubOrgClient.org method and tests
        that the result of _public_repos_url is the expected one based
        on the mocked payload.
        """
        # Known payload to be returned by the mocked org method
        mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/example/repos"
        }
        client = GithubOrgClient("example")

        result = client._public_repos_url

        expected_url = "https://api.github.com/orgs/example/repos"  

        self.assertEqual(result, expected_url)
