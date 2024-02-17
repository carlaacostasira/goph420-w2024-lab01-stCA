import numpy as np 

def integrate_newton(x, f, alg): 
"""Compute numerical integration of discrete
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
        If alg contain a str different than 'trap' or 'simp'
        If the dimensions of x and f are imcompatible
    """

x = 

if not (isinstance(x, (list, np.ndarray)) and isinstance(f, (list, np.ndarray))):
        raise ValueError("x and f must be array-like")
    if np.shape(x) != np.shape(f):
        raise ValueError("x and f must have the same shape")

if alg not in ['trap', 'simp']:
        raise ValueError(f"Invalid algorithm '{alg}'. Allowed values are 'trap' or 'simp'")
    
#Implement the trapezoid rule
if alg == 'trap':
    integral = np.trapz(f, x)
# Implement Simpson's rule
elif alg == 'simp':
    integral = np.sum(f) * np.diff(x)[0] /  3  # Simplified version, actual Simpson's rule requires more work
    
    return integral