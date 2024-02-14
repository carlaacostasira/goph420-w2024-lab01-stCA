def integrate_newton(x): 
"""Compute numerical integration of discrete
   data using Newton-Cotes rules.

    Inputs
    ------
    x : array_like
        Coordinates of sampling points
    f : array_like
        Values of thesampling points
    alg : str
        
    Returns
    -------
    float

    Raises
    ------
    ValueError
        If alg contain a str 
    """