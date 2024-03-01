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
    dx = x[1] - x[0]

# Calculating the integration with trapezoid rule
    if alg == 'trap':
        integral = (0.5*dx) * (fo +  2 * np.sum(f[1:-1]) + fn)

    #Calculating the integration with Simpson's rule
    elif alg == 'simp': 
        if N % 2: #If there are odd number of segments
            integral =  ((dx)/(3)) * (f[0] 
                                    + 4 * np.sum(f[1:-4:2]) 
                                    + 2 * np.sum(f[2:-4:2]) 
                                    + f[-4]) 
            
            integral += ((3*dx)*0.125) * (f[-4] 
                                     + 3 * f[-3] 
                                     + 3 * f[-2] 
                                     + f[-1]) #Perform Simp 1/3 + 3/8 for the last 4 points
                       
        else: 
            integral = (dx)/(3) * (f[0] 
                                            + 4 * np.sum(f[1:-1:2]) 
                                            + 2 * np.sum(f[2:-1:2]) 
                                            + f[-1]) #Perform Simp 1/3  

    return float(integral)