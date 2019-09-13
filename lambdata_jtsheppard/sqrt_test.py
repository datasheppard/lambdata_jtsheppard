import unittest
import numpy as np

from sqrt import newton_sqrt1, lazy_sqrt, builtin_sqrt
class SqrtTests(unittest.TestCase):
    '''Class to test square root functions'''

    def test_lazy_sqrt(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_newton_sqrt1(self):
        self.assertAlmostEqual(newton_sqrt1(2), 1.41421356)

if __name__ == "__main__":
    unittest.main()
