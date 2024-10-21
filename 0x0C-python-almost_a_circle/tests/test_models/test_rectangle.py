#!/usr/bin/python3
""" Module for testing rectange.py"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test the Rectangle class."""

    def test_init(self):
        """Test the initialization of Rectangle instances."""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        r2 = Rectangle(5, 15, 2, 3, 12)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 12)

    def test_width_setter(self):
        """Test the width setter."""
        r = Rectangle(10, 20)
        r.width = 15
        self.assertEqual(r.width, 15)

        with self.assertRaises(ValueError):
            r.width = -1

        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter(self):
        """Test the height setter."""
        r = Rectangle(10, 20)
        r.height = 25
        self.assertEqual(r.height, 25)

        with self.assertRaises(ValueError):
            r.height = -5

        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_setter(self):
        """Test the x setter."""
        r = Rectangle(10, 20)
        r.x = 5
        self.assertEqual(r.x, 5)

        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter(self):
        """Test the y setter."""
        r = Rectangle(10, 20)
        r.y = 3
        self.assertEqual(r.y, 3)

        with self.assertRaises(ValueError):
            r.y = -2


if __name__ == "__main__":
    unittest.main()
