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
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts3(self):
        actual = integrate_gauss(self.f,self.x, npts=3)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts4(self):
        actual = integrate_gauss(self.f,self.x, npts=4)
        self.assertAlmostEqual(actual, self.expected)
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)
    
class TestIntegrateGaussPoly_2ndOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**2 + 2*x - 1
        self.expected = ((1/3) * self.x[-1]**3 
                         + self.x[-1]**2 - self.x[-1] 
                         - ((1/3) * self.x[0]**3 
                            + self.x[0]**2 - self.x[0]))    
    
    def test_integral_value_npts2(self):
        actual = integrate_gauss(self.f,self.x, npts=2)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts3(self):
        actual = integrate_gauss(self.f,self.x, npts=3)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts4(self):
        actual = integrate_gauss(self.f,self.x, npts=4)
        self.assertAlmostEqual(actual, self.expected)
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)

class TestIntegrateGaussPoly_3rdOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**3 + x**2 + 2*x - 1
        self.expected = ((1/4) * self.x[-1]**4 + (1/3) * self.x[-1]**3 
                         + self.x[-1]**2 - self.x[-1] 
                    - ((1/4) * self.x[0]**4 + (1/3) * self.x[0]**3 
                       + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts2(self):
        actual = integrate_gauss(self.f,self.x, npts=2)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts3(self):
        actual = integrate_gauss(self.f,self.x, npts=3)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts4(self):
        actual = integrate_gauss(self.f,self.x, npts=4)
        self.assertAlmostEqual(actual, self.expected)
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)

class TestIntegrateGaussPoly_4thOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**4 + x**3 + x**2 + 2*x - 1
        self.expected = ((1/5) * self.x[-1]**5 + (1/4) * self.x[-1]**4 
                         + (1/3) * self.x[-1]**3 + self.x[-1]**2 - self.x[-1] 
                    - ((1/5) * self.x[0]**5 + (1/4) * self.x[0]**4 
                       + (1/3) * self.x[0]**3 + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts3(self):
        actual = integrate_gauss(self.f,self.x, npts=3)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts4(self):
        actual = integrate_gauss(self.f,self.x, npts=4)
        self.assertAlmostEqual(actual, self.expected)
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)

class TestIntegrateGaussPoly_5thOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**5 + x**4 + x**3 + x**2 + 2*x - 1
        self.expected = ((1/6) * self.x[-1]**6 + (1/5) * self.x[-1]**5 
                         + (1/4) * self.x[-1]**4 + (1/3) * self.x[-1]**3 
                         + self.x[-1]**2 - self.x[-1] 
                    - ((1/6) * self.x[0]**6 + (1/5) * self.x[0]**5 
                       + (1/4) * self.x[0]**4 + (1/3) * self.x[0]**3 
                       + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts3(self):
        actual = integrate_gauss(self.f,self.x, npts=3)
        self.assertAlmostEqual(actual, self.expected)
        
    def test_integral_value_npts4(self):
        actual = integrate_gauss(self.f,self.x, npts=4)
        self.assertAlmostEqual(actual, self.expected)
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)
        
class TestIntegrateGaussPoly_6thOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**6 + x**5 + x **4 + x**3 + x**2 + 2*x - 1
        self.expected = ((1/7) * self.x[-1]**7 + (1/6) * self.x[-1]**6 
                         + (1/5) * self.x[-1]**5 + (1/4) * self.x[-1]**4 
                         + (1/3) * self.x[-1]**3 + self.x[-1]**2 - self.x[-1] 
                    - ((1/7) * self.x[0]**7 + (1/6) * self.x[0]**6 
                       + (1/5) * self.x[0]**5 + (1/4) * self.x[0]**4 
                       + (1/3) * self.x[0]**3 + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts4(self):
        actual = integrate_gauss(self.f,self.x, npts=4)
        self.assertAlmostEqual(actual, self.expected)
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)

class TestIntegrateGaussPoly_7thOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**7 + x**6 + x**5 + x **4 + x**3 + x**2 + 2*x - 1
        self.expected = ((1/8) * self.x[-1]**8 + (1/7) * self.x[-1]**7 
                         + (1/6) * self.x[-1]**6 + (1/5) * self.x[-1]**5 
                         + (1/4) * self.x[-1]**4 + (1/3) * self.x[-1]**3 
                         + self.x[-1]**2 - self.x[-1] 
                    - ((1/8) * self.x[0]**8 + (1/7) * self.x[0]**7 
                       + (1/6) * self.x[0]**6 + (1/5) * self.x[0]**5 
                       + (1/4) * self.x[0]**4 + (1/3) * self.x[0]**3 
                       + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts4(self):
        actual = integrate_gauss(self.f,self.x, npts=4)
        self.assertAlmostEqual(actual, self.expected)
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)

class TestIntegrateGaussPoly_8thOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**8 + x**7 + x**6 + x**5 + x **4 + x**3 + x**2 + 2*x - 1
        self.expected = ((1/9) * self.x[-1]**9 + (1/8) * self.x[-1]**8 
                         + (1/7) * self.x[-1]**7 + (1/6) * self.x[-1]**6 
                         + (1/5) * self.x[-1]**5 + (1/4) * self.x[-1]**4 
                         + (1/3) * self.x[-1]**3 + self.x[-1]**2 - self.x[-1] 
                    - ((1/9) * self.x[0]**9 + (1/8) * self.x[0]**8 
                       + (1/7) * self.x[0]**7 + (1/6) * self.x[0]**6 
                       + (1/5) * self.x[0]**5 + (1/4) * self.x[0]**4 
                       + (1/3) * self.x[0]**3 + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)

class TestIntegrateGaussPoly_9thOrder(unittest.TestCase):
    def setUp(self):
        self.x = [-2,2]
        self.f = lambda x: x**9 + x**8 + x**7 + x**6 + x**5 + x **4 + x**3 + x**2 + 2*x - 1
        self.expected = ((1/10) * self.x[-1]**10 + (1/9) * self.x[-1]**9 + (1/8) * self.x[-1]**8 
                         + (1/7) * self.x[-1]**7 + (1/6) * self.x[-1]**6 
                         + (1/5) * self.x[-1]**5 + (1/4) * self.x[-1]**4 
                         + (1/3) * self.x[-1]**3 + self.x[-1]**2 - self.x[-1] 
                    - ((1/10) * self.x[0]**10 + (1/9) * self.x[0]**9 + (1/8) * self.x[0]**8 
                       + (1/7) * self.x[0]**7 + (1/6) * self.x[0]**6 
                       + (1/5) * self.x[0]**5 + (1/4) * self.x[0]**4 
                       + (1/3) * self.x[0]**3 + self.x[0]**2 - self.x[0]))
    
    def test_integral_value_npts5(self):
        actual = integrate_gauss(self.f,self.x, npts=5)
        self.assertAlmostEqual(actual, self.expected)

class TestFixedQuadNonPoly(unittest.TestCase):
    def test_FixedQuad_npts1(self):
        self.x = [0, (np.pi)]
        self.f = lambda x: np.cos(x) + np.sin(x)
        npts_values = [1,2,3,4,5]
        
        for npts in npts_values:
            gauss_result = integrate_gauss(self.f, self.x, npts=npts)
            fixed_quad_result, _ = fixed_quad(self.f, 0, np.pi, n=npts)
            self.assertAlmostEqual(gauss_result, fixed_quad_result)
        
class TestFixedQuadPoly(unittest.TestCase):
    def setUp(self):
        self.x = [0, 3]
        self.f = lambda x: x**2 + x**3 + 1
        npts_values = [1,2,3,4,5]
        
        for npts in npts_values:
            gauss_result = integrate_gauss(self.f, self.x, npts=npts)
            fixed_quad_result, _ = fixed_quad(self.f, 0, 3, n=npts)
            self.assertAlmostEqual(gauss_result, fixed_quad_result)        
        
if __name__ == '__main__':
    unittest.main()