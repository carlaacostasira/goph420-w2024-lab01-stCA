import unittest
import numpy as np
from scipy.integrate import fixed_quad
from goph420_lab01.integration import integrate_gauss

class TestIntegrateGaussPoly(unittest.TestCase):

    def test_polynomials(self):
        # Define polynomial orders and corresponding coefficients
        orders = range(1, 10) # Polynomials of orders 1 to 9
        coeffs = [np.random.rand(order) for order in orders]

        for order, coeff in zip(orders, coeffs):
            # Generate polynomial function
            def f(x):
                return np.polyval(coeff, x)

            # Calculate exact integral
            exact_integral = np.polyint(coeff)(1) - np.polyint(coeff)(0)

            # Test with npts=1 to 5
            for npts in range(1, 6):
                # Use integrate_gauss with npts
                result = integrate_gauss(f, [0, 1], npts=npts)
                self.assertAlmostEqual(result, exact_integral, delta=1e-5)

    def test_non_polynomial_function(self):
        # Define a non-polynomial function
        def f(x):
            return x**2

        # Calculate exact integral
        exact_integral = 1/3

        # Test with npts=1 to 5
        for npts in range(1, 6):
            # Use integrate_gauss with npts
            result = integrate_gauss(f, [0, 1], npts=npts)
            self.assertAlmostEqual(result, exact_integral, delta=1e-5)

    def test_against_fixed_quad(self):
        # Define a test function
        def f(x):
            return x**2

        # Test with npts=1 to 5
        for npts in range(1, 6):
            # Use integrate_gauss with npts
            gauss_result = integrate_gauss(f, [0, 1], npts=npts)

            # Use scipy.integrate.fixed_quad with the same number of points
            fixed_quad_result, _ = fixed_quad(f, 0, 1, n=npts)

            # Compare the results
            self.assertAlmostEqual(gauss_result, fixed_quad_result, delta=1e-5)
        
if __name__ == '__main__':
    unittest.main()