import unittest
import numpy as np
import sys
import math 
sys.path.append('/Users/carla/Repos/goph420-w2024-lab01-stCA/src')
from goph420_lab01 import integration
from goph420_lab01.integration import integrate_newton

x = np.linspace(-15, 15, num=500)
f = 2*x**2 + 2*x

class TestIntegration(unittest.TestCase):

    def test_upper(self):
        Exact_integral = (2/3  * x[-1]**3 + x[-1]**2) - (2/3  * x[0]**3 + x[0]**2)
        Compute_integral = integrate_newton(x,f,'trap')
        self.assertAlmostEqual(Compute_integral, Exact_integral, delta=1e-1)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
