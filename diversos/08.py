import numpy as np
import matplotlib.pyplot as plt

# Sample data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11, 13])

# Fit a linear polynomial (degree = 1)
coefficients = np.polyfit(x, y, 1)

# Generate fitted y-values
y_fit = np.polyval(coefficients, x)

print("coefficients : ", coefficients)

print("slope  : ", coefficients[0])

print("intercept   : ", coefficients[1])



# Plot original data and the fitted line
plt.scatter(x, y, label='Original Data', color='red')
plt.plot(x, y_fit, label='Fitted Line', color='blue')
plt.legend()
plt.show()