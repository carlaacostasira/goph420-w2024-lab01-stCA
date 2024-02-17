def integrate_newton(x, f, alg): 
"""Compute numerical integration of discrete
   data using Newton-Cotes rules.

    Inputs
    ------
    x : array_like
        Coordinates of sampling points given by the time [s]
    f : array_like
        Values of the sampling points given by the velocity [mm/s]
    alg : str 
        Default value of 'trap' or 'simp' 
        
    Returns
    -------
    I : float
        Integral estimate

    Raises
    ------
    ValueError
        If alg contain a str different than 'trap' or 'simp'
        If the dimensions of x and f are imcompatible
    """

x = 
