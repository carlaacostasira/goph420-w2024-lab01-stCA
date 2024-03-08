import numpy as np
import matplotlib.pyplot as plt
from goph420_lab01.integration import integrate_newton
from goph420_lab01.integration import integrate_gauss

# Initial data to make the calculations
g = 3.718 #[m/s^2]
m = 93.0 #[kg]
c = 47.0 #[kg/s]
v_o = 100 #[m/s]
v_f = g * m / c #[m/s] Approx elocity at t=20s

dt_1s = np.arange(0, 21, 1) # Defining the step sizes in the time interval every 1 s
dt_2s = np.arange(0, 21, 2) # Defining the step sizes in the time interval every 2 s

velocity_1 = v_f + (v_o - v_f) * np.exp((- c/m)*dt_1s) # Generating the functions with the time values
velocity_2 = v_f + (v_o - v_f) * np.exp((- c/m)*dt_2s) #

#Part a)
Integration_1 = (integrate_newton(dt_1s,velocity_1,'trap')) # Applying integrate newton formula ofr trap rule
Integration_2 = (integrate_newton(dt_2s,velocity_2,'trap')) #

print(f"The integral value using the trapezoidal rule with \u0394t = 1s is {round(Integration_1, 8)}")
print(f"The integral using the trapezoidal rule with \u0394t = 2s is {round(Integration_2, 8)}")

#Part b)

Integration_3 = (integrate_newton(dt_1s,velocity_1,'simp')) # Applying integrate newton formula ofr simp rule
Integration_4 = (integrate_newton(dt_2s,velocity_2,'simp'))

print(f"The integral value using the Simpson's 1/3 rule with \u0394t = 1s is {round(Integration_3, 8)}")
print(f"The integral using the Simpson's 1/3 rule with \u0394t = 2s is {round(Integration_4, 8)}")

#Part c) Defening the function to calculate the integrate gauss 
lims = [0, 20]
def velocity_function(t):
    function = v_f + (v_o - v_f) * np.exp(-(c/m)*t)
    return function

Integration_5 = integrate_gauss(velocity_function, lims, 5)

print(f"The integral using the Gausss Quadrature {Integration_5}") 
