#!/usr/bin/python3
""" test_base.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the number of Base objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_none(self):
        """Test when id is not provided."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_provided(self):
        """Test when a specific id is provided."""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_mixed_id(self):
        """Test mixed cases of provided and not provided ids."""
        b4 = Base()
        b5 = Base(99)
        b6 = Base()
        self.assertEqual(b4.id, 1)
        self.assertEqual(b5.id, 99)
        self.assertEqual(b6.id, 2)

    def test_id_after_provided(self):
        """Test id auto-increment after an id is provided."""
        b7 = Base(7)
        b8 = Base()
        self.assertEqual(b7.id, 7)
        self.assertEqual(b8.id, 1)


if __name__ == "__main__":
    unittest.main()
