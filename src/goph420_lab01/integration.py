import numpy as np 

def integrate_newton(x, f, alg): 
"""
Compute numerical integration of discrete
   data using Newton-Cotes rules.

    Inputs
    ------
    x : array_like
    f : array_like
    alg : str 
        Default value of 'trap' or 'simp' 
        
    Returns
    -------
    integral : float
        Integral estimate

    Raises
    ------
    ValueError
        If the dimensions of x and f are imcompatible
        If alg contain a str different than 'trap' or 'simp'
    """



if not (isinstance(x, (list, np.ndarray)) and isinstance(f, (list, np.ndarray))): # Comparing if x and f are array-like w/ same shape
    raise ValueError("x and f must be array-like")
if np.shape(x) != np.shape(f):
    raise ValueError("x and f must have the same shape")

if alg not in ['trap', 'simp']: #Evaluating f the imput is trap or simp, otherwise will come up an error 
    raise ValueError(f"Invalid '{alg}'. Allowed values are 'trap' or 'simp'")

# Calculating the integration with trapezoid rule
if alg == 'trap':
    integral =  0.5 * (x[-1] - x[0]) * (f[0] +  2 * sum(f[1:N-1]) + f[-1])
    
#Calculating the integration with Simpson's rule
elif alg == 'simp': #How can I set up a condition that count the # of segments or points
#    for i in a range(1:N)
#        if i % 2 == 0:
#            integral =  (x[-1] - x[0])/3 * (f[0] + 4 * sum(f[1:2*i-1] + 2 * f[2:2*i] + f[-1]))
#        else:
#            integral 


    return integral




def integrate_gauss(f, lims, npts=3):
    # Check if f is callable
    if not callable(f):
        raise TypeError("f must be a callable object")
    
    # Check if lims has length  2
    if not isinstance(lims, (list, tuple)) or len(lims) !=  2:
        raise ValueError("lims must be an iterable with  2 elements")
    
    # Check if lims[0] and lims[1] can be converted to float
    try:
        a = float(lims[0])
        b = float(lims[1])
    except (ValueError, TypeError):
        raise ValueError("lims must contain two numbers that can be converted to float")
    
    # Check if npts is in the allowed set
    if npts not in [1,  2,  3,  4,  5]:
        raise ValueError("npts must be one of [1,  2,  3,  4,  5]")
    
    # Use numpy's linspace to generate the points
    x = np.linspace(a, b, npts)
    
    # Apply the Gaussian quadrature method
    # This is a simplified example and does not include the actual Gauss-Legendre points
    # For a real implementation, you would need to use the actual Gauss-Legendre points
    integral =  0.0
    for i in range(npts):
        integral += f(x[i])
    
    # Multiply by the interval width divided by the number of points
    integral *= (b - a) / npts
    
    return integral
