import io
import unittest
from unittest.mock import patch

from Matrix_test import m_transp

class TestTriangle(unittest.TestCase):

    def test_type(self):
        self.assertRaises(TypeError, m_transp, "2, 2, 3")

    def test_value(self):
        with self.assertRaises(ValueError):
            m_transp([[1,2], [3,4,5], [6,7,8]])


if __name__ == '__main__':
    unittest.main(verbosity=2)