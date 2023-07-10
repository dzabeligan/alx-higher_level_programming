#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """
    Test case class for the max_integer function.
    """

    def test_ordered_list(self):
        """
        Test an ordered list of integers.
        """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """
        Test an unordered list of integers.
        """
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """
        Test a list with a maximum value at the beginning.
        """
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_max_at_end(self):
        """
        Test a list with a maximum value at the end.
        """
        max_at_end = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_at_end), 4)

    def test_duplicate_values(self):
        """
        Test a list with duplicate values.
        """
        duplicate_values = [3, 3, 2, 1, 2]
        self.assertEqual(max_integer(duplicate_values), 3)

    def test_negative_values(self):
        """
        Test a list with negative values.
        """
        negative_values = [-4, -2, -1, -3]
        self.assertEqual(max_integer(negative_values), -1)

    def test_mixed_values(self):
        """
        Test a list with mixed integer and float values.
        """
        mixed_values = [1, 2, 3.5, 2.8, 4]
        self.assertEqual(max_integer(mixed_values), 4)

    def test_empty_list(self):
        """
        Test an empty list.
        """
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)


if __name__ == '__main__':
    unittest.main()
