# This file contains example tests.
#
# @package      namespace.pybase
# @author       Matt Koskela <mattkoskela@gmail.com>
##

"""
test_example.py

Unit tests for namespace.pybase
"""

import unittest
from namespace.pybase import Example


class TestPyBase(unittest.TestCase):
    """Tests all methods in namespace.pybase class."""

    def setUp(self):
        """This sets up the example tests"""

        self.test = Example.Math()

    def tearDown(self):
        """ This tears down the sample tests"""

        self.test = None
    
    def test_add_stuff(self):
        """ Tests Math.add_stuff() """

        self.test.add_stuff(1,2,3,4)
        x = self.test.total
        self.assertEqual(x, 10)

    def test_reset(self):
        """ Tests Math.reset() function""" 

        self.test.add_stuff(1,2,3,4)
        self.test.reset()
        self.assertEqual(self.test.total, 0)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
