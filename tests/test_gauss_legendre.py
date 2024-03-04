import unittest
import numpy as np
from goph420_lab01.integration import integrate_gauss

class TestIntegrationGaussPolynomial(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(-4, 4) 
        self.f = 2*self.x**3 + 3*self.x**2 + 5*self.x + 4
    
    def test_integral_value(self):
        expected = (0.5 * self.x[-1]**4 
                        + self.x[-1])**3 
                        + (5*0.5) * self.x[-1]**2 
                        + 4 * self.x[-1] 
                        - ((0.5 * self.x[0]**4 
                        + self.x[0])**3 
                        + (5 * 0.5) * self.x[0]**2 
                        + 4 * self.x[0]) 
        actual = integrate_gauss(self.f, self.x, 5)
        self.assertAlmostEqual(actual, expected)

class TestIntegrationGaussNonPolynomial(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(-np.pi(), np.pi()) 
        self.f = 3*np.cos(self.x) + 2*np.sin(self.x)
    
    def test_integral_value(self):
        expected = (3 * np.sin(self.x[-1]) 
                    - 2 * np.cos(self.x[-1])) 
                    - (3 * np.sin(self.x[0]) 
                    - 2 * np.cos(self.x[0])) 
        actual = integrate_gauss(self.f, self.x, 5)
        self.assertAlmostEqual(actual, expected)