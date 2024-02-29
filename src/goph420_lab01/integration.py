import numpy as np 

def integrate_newton(x, f, alg): 
# """
# Compute numerical integration of discrete
#    data using Newton-Cotes rules.

#     Inputs
#     ------
#     x : array_like
#     f : array_like
#     alg : str 
#         Default value of 'trap' or 'simp' 
        
#     Returns
#     -------
#     integral : float
#         Integral estimate

#     Raises
#     ------
#     ValueError
#         If the dimensions of x and f are imcompatible
#         If alg contain a str different than 'trap' or 'simp'
#     """

    if not (isinstance(x, np.ndarray) and isinstance(f, np.ndarray)): # Comparing if x and f are array-like w/ same shape
        raise ValueError("x and f must be array-like")
    if np.shape(x) != np.shape(f):
        raise ValueError("x and f must have the same shape")

    if alg not in ['trap', 'simp']: #Evaluating f the imput is trap or simp, otherwise will come up an error 
        raise ValueError(f"Invalid '{alg}'. Allowed values are 'trap' or 'simp'")

    a = x[0]
    b = x[-1]
    fo = f[0]
    fn = f[-1]
    N = len(x) - 1

# Calculating the integration with trapezoid rule
    if alg == 'trap':
        integral =  ((b-a)/(2*N)) * (fo +  2 * sum(f[1:-1]) + fn)

    #Calculating the integration with Simpson's rule
    elif alg == 'simp': 
        if N % 2 == 1: #If there are odd number of segments
            integral =  (x[-4] - x[0])/(3*(N-2)) * (f[0] + 4 * sum(f[1:-4:2] + 2 * f[2:-4:2] + f[-4])) + ((x[-1] - x[-4])/8) * (f[-4] + 3 * f[-3] + 3 * f[-2] + f[-1]) #Perform Simp 1/3 + 3/8 for the last 4 points 
        else: 
            integral = (x[-1] - x[0])/(3*(N)) * (f[0] + 4 * sum(f[1:-4:2] + 2 * f[2:-4:2] + f[-1])) #Perform Simp 1/3  

    return float(integral)

# def integrate_gauss(f, lims, npts=3):
#     # Check if f is callable
#     if not callable(f):
#         raise TypeError("f must be a callable object")
    
#     # Check if lims has length  2
#     if not isinstance(lims, (list, tuple)) or len(lims) !=  2:
#         raise ValueError("lims must be an iterable with  2 elements")
    
#     # Check if lims[0] and lims[1] can be converted to float
#     try:
#         a = float(lims[0])
#         b = float(lims[1])
#     except (ValueError, TypeError):
#         raise ValueError("lims must contain two numbers that can be converted to float")
    
#     # Check if npts is in the allowed set
#     if npts not in [1,  2,  3,  4,  5]:
#         raise ValueError("npts must be one of [1,  2,  3,  4,  5]")
    
#     # Use numpy's linspace to generate the points
#     x = np.linspace(a, b, npts)
    
#     # Apply the Gaussian quadrature method
#     # This is a simplified example and does not include the actual Gauss-Legendre points
#     # For a real implementation, you would need to use the actual Gauss-Legendre points

# x_k= [0, 0.57735, 0, 0.774597, 0.339981, 0.861136, 0, 0.538469, 0.90618] #Points Xi
# w_k= [2, 1, 0.888889, 0.555556, 0.652145, 0.347855, 0.568889, 0.478629, 0.236927] #Weights Wi

# integral =  0.0
#     for i in range(npts):
#         integral += f(x[i])
    
#     # Multiply by the interval width divided by the number of points
#     integral *= (b - a) / npts
    
#     return integral
