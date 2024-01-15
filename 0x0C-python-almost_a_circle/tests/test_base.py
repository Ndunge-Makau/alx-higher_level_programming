#!/usr/bin/python3
"""Unittest for Base.py"""
import unittest
from models.base import Base


class TestBaseInit(unittest.TestCase):
    """Tests the Base Module"""

    def test_init_id(self):
        """Test object initialization with id given"""
        base1 = Base(12)
        self.assertEqual(base1.id, 12)

    def test_init_no_id(self):
        """Test object init with no id given"""
        base1 = Base()
        self.assertEqual(base1.id, 1)


if __name__ == '__main__':
    unittest.main()
