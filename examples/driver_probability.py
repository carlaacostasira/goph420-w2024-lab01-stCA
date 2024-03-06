import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from goph420_lab01.integration import integrate_gauss

# Define the mean and standard deviation
mu = 1.5 # Mean of the distribution
sigma = 0.5 # Standard deviation of the distribution
magnitude = 4.0
z = (magnitude - mu)/sigma
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
# Calculate the PDF for the standard normal distribution at each x value
pdf_values = norm.pdf(x, mu, sigma)

# Plot the PDF
plt.plot(x, pdf_values)
plt.title('Standard Normal Distribution PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
