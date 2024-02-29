import unittest
import numpy as np
import sys
import math 
sys.path.append('/Users/carla/Repos/goph420-w2024-lab01-stCA/src')
from goph420_lab01 import integration
from goph420_lab01.integration import integrate_newton

x_trap = np.linspace(-15, 15, num=750) #Linear function
f_trap = 2*x_trap + 3

x_odd = np.linspace(-15, 15, num=751) #Quadratic function odd number of data points
f_odd = x_odd**2 + 4*x_odd

x_even = np.linspace(-15, 15, num=750) #Quadratic function even number of data points
f_even = x_even**2 + 4*x_even

class TestIntegration(unittest.TestCase):

    def test_upper(self):
        Exact_integral = (x_trap[-1]**2 + 3 * x_trap[-1]) - (x_trap[0]**2 + 3 * x_trap[0]) #Result = 90
        Compute_integral_even_trap = integrate_newton(x_trap,f_trap,'trap')
        self.assertAlmostEqual(Compute_integral_even_trap, Exact_integral, delta=1e-1)

    def test_upper(self):
        Exact_integral_even = (1/3  * x_even[-1]**3 + 2 * x_even[-1]**2) - (1/3  * x_even[0]**3 + 2 * x_even[0]**2) # Result = 2250
        Exact_integral_odd = (1/3  * x_odd[-1]**3 + 2 * x_odd[-1]**2) - (1/3  * x_odd[0]**3 + 2 * x_odd[0]**2) # Result = 2250
        Compute_integral_even = integrate_newton(x_even,f_even,'simp')
        Compute_integral_odd = integrate_newton(x_odd,f_odd,'simp')
        self.assertAlmostEqual(Compute_integral_even, Exact_integral_even, delta=1e-1)
        self.assertAlmostEqual(Compute_integral_odd, Exact_integral_odd, delta=1e-1)

if __name__ == '__main__':
    unittest.main()
