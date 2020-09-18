#!/usr/bin/env python
"""
Test cases for templating engine.
"""
import unittest
from cli.template import print_test, to_sql


class TestTemplate(unittest.TestCase):
    """
    Test cases.
    """

    def test_print(self):
        """Test case."""
        print_test()
        self.assertIs(1, 1)

    def test_template(self):
        """
        Test template.
        """
        to_sql()
        self.assertIs(1, 1)


if __name__ == "__main__":
    unittest.main()
