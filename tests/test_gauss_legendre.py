import unittest
import numpy as np
from scipy.integrate import fixed_quad
from goph420_lab01.integration import integrate_gauss

class TestIntegrateGaussPoly_1stOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: 2*x - 1
        self.expected = (self.x[-1]**2 - self.x[-1] - (self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts1(self):
        actual = integrate_gauss(self.f,self.x, npts=1)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts2(self):
        actual = integrate_gauss(self.f,self.x, npts=2)
        self.assertAlmostEqual(actual, self.expected) #continue
    
class TestIntegrateGaussPoly_2ndOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**2 + 2*x - 1
        self.expected = ((1/3) * self.x[-1]**3 + self.x[-1]**2 - self.x[-1] - ((1/3) * self.x[0]**3 + self.x[0]**2 - self.x[0]))    
    
    def test_integral_value_npts2(self):
        actual = integrate_gauss(self.f,self.x, npts=2)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts3(self):
        actual = integrate_gauss(self.f,self.x, npts=3)
        self.assertAlmostEqual(actual, self.expected)

class TestIntegrateGaussPoly_3rdOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**3 + x**2 + 2*x - 1
        self.expected = ((1/4) * self.x[-1]**4 + (1/3) * self.x[-1]**3 + self.x[-1]**2 - self.x[-1] 
                    - ((1/4) * self.x[0]**4 + (1/3) * self.x[0]**3 + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts2(self):
        actual = integrate_gauss(self.f,self.x, npts=2)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts3(self):
        actual = integrate_gauss(self.f,self.x, npts=3)
        self.assertAlmostEqual(actual, self.expected)

# class TestIntegrateGaussPoly_4thOrder(unittest.TestCase):
#     def setUp(self):
#         self.x = [-2,2]
#         self.f = lambda x: self.x **4 + self.x**3 + self.x**2 + 2*self.x - 1
    
#     def test_integral_value(self):
#         expected = ((1/5) * self.x[-1]**5 + (1/4) * self.x[-1]**4 + (1/3) * self.x[-1]**3 + self.x[-1]**2 - 1 
#                     - ((1/5) * self.x[0]**5 + (1/4) * self.x[0]**4 + (1/3) * self.x[0]**3 + self.x[0]**2 - 1)) 
#         for npts in range(1, 6): 
#             actual = integrate_gauss(self.f,self.x, npts=npts)
#             self.assertAlmostEqual(actual, expected)

# class TestIntegrateGaussPoly_5thOrder(unittest.TestCase):
#     def setUp(self):
#         self.x = np.linspace(-2, 2)
#         self.f = self.x **5 + self.x **4 + self.x**3 + self.x**2 + 2*self.x - 1
    
#     def test_integral_value(self):
#         expected = ((1/6) * self.x[-1]**6 + (1/5) * self.x[-1]**5 + (1/4) * self.x[-1]**4 + (1/3) * self.x[-1]**3 + self.x[-1]**2 - 1 
#                     - ((1/6) * self.x[0]**6 + (1/5) * self.x[0]**5 + (1/4) * self.x[0]**4 + (1/3) * self.x[0]**3 + self.x[0]**2 - 1)) 
#         for npts in range(1, 6): 
#             actual = integrate_gauss(self.f,self.x, npts=npts)
#             self.assertAlmostEqual(actual, expected)


# class TestIntegrateGaussNonPoly(unittest.TestCase):
#     def test_function(self):
#         # Define a non-polynomial function
#         def f(x):
#             return np.cos(x) + x

#         # Calculate exact integral
#         exact_integral = 2 * np.pi**2 / 2

#         # Test with npts=1 to 5
#         for npts in range(1, 6):
#             # Use integrate_gauss with npts
#             result = integrate_gauss(f, [0, 2*np.pi], npts=npts)
#             self.assertAlmostEqual(result, exact_integral)
            
# class TestFixedQuad(unittest.TestCase):
#     def test_fixed_quad(self):
#         # Define a test function
#         def f(x):
#             return np.sin(x)

#         # Test with npts=1 to 5
#         for npts in range(1, 6):
#         # Use integrate_gauss with npts
#             gauss_result = integrate_gauss(f, [0, 2*np.pi], npts=npts)

#         # Use scipy.integrate.fixed_quad with the same number of points
#             fixed_quad_result, _ = fixed_quad(f, 0, 2*np.pi, n=npts)

#         # Compare the results
#             self.assertAlmostEqual(gauss_result, fixed_quad_result)
        
if __name__ == '__main__':
    unittest.main()