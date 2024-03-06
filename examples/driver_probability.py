import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from goph420_lab01.integration import integrate_gauss

# Define the mean and standard deviation
mean_i = 1.5 # Mean of the distribution
sd_i = 0.5 # Standard deviation of the distribution
magnitude = 2.0
z = (magnitude - mean_i)/sd_i

lims = [0, 4]
# Calculate the PDF for the standard normal distribution at each x value
def probability_function(x):
    probability_function = ((1/(np.sqrt(2*np.pi))) * np.exp( -0.5 * (z)**2))
    return probability_function

probability_event = np.empty(5)
eps_a = np.empty(4) 

npts_values = [1, 2, 3, 4, 5] # Adjusted to match the length of eps_a

for i, npts in enumerate(npts_values):
    integral = integrate_gauss(probability_function, lims, npts=npts)
    probability_event[i] = 0.5 - integral

for i in range(1, 4): # Adjusted to start from 1 to match the length of probability_event
    eps_a[i-1] = np.abs(probability_event[i] - probability_event[i-1] / probability_event[i])

print(probability_event)
print(eps_a)

# plt.plot(npts_values, eps_a, label="|\u03B5_a|", marker='o')
# plt.xscale("log")
# plt.yscale("log")
# plt.xlabel('Number of integration points')
# plt.ylabel('Approx. Relative Error, |\u03B5|')
# plt.title('Convergence plot')
# plt.legend(loc="upper left")
# plt.show()

mean_ii = 10.28
sd_ii = 0.05
lims_ii = [10.25, 10.35] 

def probability_function2(x):
    return norm.pdf(x, mean_ii, sd_ii)


true_value = np.empty(5)
eps_aii = np.empty(4) 

npts_values = [1, 2, 3, 4, 5] # Adjusted to match the length of eps_a

for i, npts in enumerate(npts_values):
    integral_ii = integrate_gauss(probability_function2, lims, npts=npts)
    true_value[i] = 0.5 - integral

for i in range(1, 4): # Adjusted to start from 1 to match the length of true_value
    eps_aii[i-1] = np.abs(true_value[i] - true_value[i-1] / true_value[i])

print(true_value)
print(eps_aii)