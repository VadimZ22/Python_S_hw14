import io
import unittest
from unittest.mock import patch

from Triangle_test import check_triangle

class TestTriangle(unittest.TestCase):

    def test_type(self):
        self.assertRaises(TypeError, check_triangle, '7')

    def test_value(self):
        with self.assertRaises(ValueError):
            check_triangle(-2, 3, 5)
            check_triangle(3, 4, 12)



if __name__ == '__main__':
    unittest.main(verbosity=2)