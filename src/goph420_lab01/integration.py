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

    N = len(x) - 1
    dx = x[1] - x[0]

# Calculating the integration with trapezoid rule
    if alg == 'trap':
        integral = (0.5*dx) * (f[0] +  2 * np.sum(f[1:-1]) + f[-1])

    #Calculating the integration with Simpson's rule
    elif alg == 'simp': 
        if N % 2: #If there are odd number of segments
            integral =  ((dx)/(3)) * (f[0] 
                                    + 4 * np.sum(f[1:-4:2]) 
                                    + 2 * np.sum(f[2:-4:2]) 
                                    + f[-4]) # Perform Simp 1/3 
            
            integral += ((3*dx)*0.125) * (f[-4] 
                                     + 3 * f[-3] 
                                     + 3 * f[-2] 
                                     + f[-1]) # Perform Simp 3/8 for the last 4 points
                       
        else: 
            integral = (dx)/(3) * (f[0] 
                                            + 4 * np.sum(f[1:-1:2]) 
                                            + 2 * np.sum(f[2:-1:2]) 
                                            + f[-1]) #Perform Simp 1/3  

    return float(integral)


def integrate_gauss(f, lims, *, npts=3):
#"""
# Compute numerical integration of discrete
#    data using Gauss Legendre.

#     Inputs
#     ------
#     f : 
#     lims : 
#     npts : 
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

    # Check if f is callable
    if not callable(f):
        raise TypeError("f must be a callable object")
    
    # Check if lims has exactly 2 elements
    if len(lims) != 2:
        raise ValueError("lims must have exactly 2 elements")
    
    # Check if lims can be converted to float
    try:
        float(lims[0])
        float(lims[1])
    except ValueError:
        raise ValueError("lims elements must be convertible to float")
    
    # Check if npts is in the allowed range
    if npts not in [1, 2, 3, 4, 5]:
        raise ValueError("npts must be one of [1, 2, 3, 4, 5]")
    
    integral = ...
    
    # Return the result 
    return float(integral)
