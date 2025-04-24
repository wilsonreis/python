import numpy as np
import matplotlib.pyplot as plt

# Sample data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11, 13])

# Fit a quadratic polynomial (degree = 2)
coefficients = np.polyfit(x, y, 2)

# Generate fitted y-values
y_fit = np.polyval(coefficients, x)

# Plot original data and the quadratic fit
plt.scatter(x, y, label='Original Data', color='red')
plt.plot(x, y_fit, label='Quadratic Fit', color='green')
plt.legend()
plt.show()