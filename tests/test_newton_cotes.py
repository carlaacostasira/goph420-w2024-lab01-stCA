import unittest
import numpy as np
from goph420_lab01.integration import integrate_newton

class TestIntegrationNewtonTrap(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(-15, 15, num=750) #Linear function
        self.f = 2*self.x + 3

    def test_integral_value(self):
        expected = (self.x[-1]**2 + 3 * self.x[-1]) - (self.x[0]**2 + 3 * self.x[0]) #Result = 90
        actual = integrate_newton(self.x,self.f,'trap')
        self.assertAlmostEqual(actual, expected)
    
    def test_integral_type(self):
        self.assertIsInstance(integrate_newton(self.x,self.f,'trap'), float)

class TestIntegrationNewtonSimpOdd(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(-15, 15, num=751) #Quadratic function odd number of data points
        self.f = self.x**2 + 4*self.x

    def test_integral_value(self):
        expected = (1/3  * self.x[-1]**3 + 2 * self.x[-1]**2) - (1/3  * self.x[0]**3 + 2 * self.x[0]**2) #Result = 2250
        actual = integrate_newton(self.x,self.f,'simp')
        self.assertAlmostEqual(actual, expected)
    
    def test_integral_type(self):
        self.assertIsInstance(integrate_newton(self.x,self.f,'simp'), float)

class TestIntegrationNewtonSimpEven(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(-15, 15, num=750) #Quadratic function odd number of data points
        self.f = self.x**2 + 4*self.x

    def test_integral_value(self):
        expected = (1/3  * self.x[-1]**3 + 2 * self.x[-1]**2) - (1/3  * self.x[0]**3 + 2 * self.x[0]**2) #Result = 2250
        actual = integrate_newton(self.x,self.f,'simp')
        self.assertAlmostEqual(actual, expected)
    
    def test_integral_type(self):
        self.assertIsInstance(integrate_newton(self.x,self.f,'simp'), float)

if __name__ == '__main__':
    unittest.main()
