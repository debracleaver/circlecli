# -*- coding: utf-8 -*-

"""
Tests for the CircleCLI API library.

"""

import unittest

from httmock import with_httmock

from circlecli import CircleAPI
import mocks.circlecli


class TestCircleCLISetup(unittest.TestCase):
    
    """ CircleAPI.init() should check the token is a 40-digit hex string
        and return an error if it is not
    """
    def test_valid_token(self):
        circlecli = CircleAPI('moo')

    def test_invalid_token(self):
        circlecli = CircleAPI('foo')

class TestCircleCLI(unittest.TestCase):
    
    def setUp(self):
        self.circlecli = CircleAPI('bar')

    @with_httmock(mocks.circlecli.resource_get)
    def test_me_false(self):
        owner = 'appneta'
        repo = 'burndown'

        results = self.circlecli.me(False)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('name' in results)
        self.assertEqual(results['name'], repo)

    @with_httmock(mocks.circlecli.resource_get)
    def test_me_true(self):
        user = 'danriti'

        results = self.circlecli.me(True)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('login' in results)
        self.assertEqual(results['login'], user)

if __name__ == '__main__':
    unittest.main()
