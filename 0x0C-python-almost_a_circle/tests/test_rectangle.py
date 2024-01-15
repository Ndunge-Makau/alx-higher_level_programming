#!/usr/bin/python3
"""
Tests the Rectangle.py module.

"""
import unittest

from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class TestRectangleInit(unittest.TestCase):
    """Tests the initialization of a Rectangle"""
    def test_init_all_args(self):
        """Tests if all args are provided"""
        rect = Rectangle(2, 4, 1, 1, 12)
        self.assertEqual(rect.id, 12)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)

    def test_init_no_id(self):
        """Tests if id attribute not provided"""
        rect = Rectangle(2, 4, 1, 1, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.y, 1)

    def test_init_no_args(self):
        """Tests for missing arguments"""
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_init_one_arg(self):
        """Tests for init with one arg"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2)

    def test_init_two_args(self):
        """Tests for two args"""
        rect = Rectangle(2, 12)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 12)

    def test_type_of_rectangle(self):
        """Tests inheritance of rectangle"""
        rect = Rectangle(2, 12, 1, 1, 12)
        self.assertIsInstance(rect, Base)

    def test_more_than_five_args(self):
        """Tests with more arguments than needed"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 1, 1, 1, 2, 5)


class TestRectangleWidth(unittest.TestCase):
    """Tests the width attribute"""
    def test_if_private(self):
        """Tests if the attribute width is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 12).__width)

    def test_None_width(self):
        """Test if width is None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle(None, 12)

    def test_str_width(self):
        """Test if width is string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle('Hello', 12)

    def test_float_width(self):
        """Test if width is float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle(0.23, 12)

    def test_negative_width(self):
        """Test if width is negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(-12, 12)


class TestRectangleHeight(unittest.TestCase):
    """Tests the height attribute"""
    def test_if_private(self):
        """Tests if the attribute height is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 12).__height)

    def test_None_height(self):
        """Test if height is None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(12, None)

    def test_str_height(self):
        """Test if height is string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(12, 'Hello')

    def test_float_height(self):
        """Test if height is float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(12, 0.23)

    def test_negative_height(self):
        """Test if height is negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(12, -12)


class TestRectangleX(unittest.TestCase):
    """Tests the x attribute"""
    def test_if_private(self):
        """Tests if the attribute x is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 12, 1, 2).__x)

    def test_None_x(self):
        """Test if x is None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(12, 12, None, 1)

    def test_str_x(self):
        """Test if x is string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(12, 12, 'Hello', 1)

    def test_float_x(self):
        """Test if x is float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(12, 12, 0.23, 1)

    def test_negative_x(self):
        """Test for negative x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect = Rectangle(12, 12, -1, 1)


class TestRectangleY(unittest.TestCase):
    """Tests the y attribute"""
    def test_if_private(self):
        """Tests if the attribute y is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 12, 1, 2).__y)

    def test_None_y(self):
        """Test if y is None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(12, 12, 1, None)

    def test_str_y(self):
        """Test if y is a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(12, 12, 1, 'Hello')

    def test_float_y(self):
        """Test if y is a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(12, 12, 1, 0.23)

    def test_negative_y(self):
        """Test for negative y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect = Rectangle(12, 12, 1, -3)


class TestArea(unittest.TestCase):
    """Tests the area() method"""
    def test_small(self):
        """Test when lengths are small"""
        rect = Rectangle(2, 4, 1, 1)
        self.assertEqual(rect.area(), 8)

    def test_large(self):
        """Test when lengths are large"""
        rect = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(rect.area(), 999999999999998999000000000000001)


"""
class TestPresentation(unittest.TestCase):
    Tests the display function
    def test_display(self):
        Checks for display
        my_display = io.StringIO()
        rect = Rectangle(1, 2)
        rect.display()
        my_display = sys.stdout
        self.assertEqual("\n#\n#\n", my_display.getvalue())

    def test_str_rep(self):
        Checks for __str__ representation
        my_display = io.StringIO()
        rect = Rectangle(1, 2, 1, 1, 12)
        print(rect)
        my_display = sys.__stdout__
        self.assertEqual("[Rectangle] (12) 1/1 - 1/2", my_display.read())

"""


if __name__ == '__main__':
    unittest.main()
