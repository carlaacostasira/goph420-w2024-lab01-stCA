import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from goph420_lab01.integration import integrate_gauss

# Define the mean and standard deviation
mu1 = 1.5 # Mean of the distribution
sigma1 = 0.5 # Standard deviation of the distribution

x = np.linspace(mu1 - 3*sigma1, mu1 + 3*sigma1, 100)

z = (x - mu1)/sigma1

# Calculate the PDF for the standard normal distribution at each x value
pdf_values = norm.pdf(x, mu1, sigma1)

# Plot the PDF
plt.plot(x, pdf_values)
plt.title('Standard Normal Distribution PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
