#!/usr/bin/python3
"""
Tests for the 6-max_integer_test.py module.

"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    """Tests the max_integer function"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 32, 4, 100]), 100)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([34, 2, 3, 4]), 34)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertRaises(TypeError, max_integer, 1)

