# GOPH 420 - Inversion Parameter Estimation for Geophysicists

*Semester: *W2024
*Instructor: *B. Karchewski
*Author: *Carla Acosta Sira

Repository for lab 01 - Numerical Integration in the GOPH 420 Course

/**
 * This folder contains the following functions:
 *
 * 1. `integrate_newton`: This function does integrate a function with Trapezoid rule and Simpson's 1/3 and 3/8 rule.  
 *    - Parameters:
 *        - `x`: sample points, array_like .
 *        - `f`: function, array_like .
 *         - `alg`: rule to be used - 'trap' or 'simp' .
 *    - Returns: integral value.
 *
 * 2. `integrate_gauss`: This function does integrate a function with the gauss legendre quadrature method
 *    - Parameters:
 *        - `f`: callable function .
 *        - `lims`: integration limits .
 *        - `npts`: number of points in the integration .
 *    - Returns: integral value.
 *
 * Usage:
 * - To use `integrate_newton`, you need to provide the input values defined and analyze your results.
 * - To use `integrate_gauss`, you need to provide the input values defined and analyze your results.
 */
/**
 