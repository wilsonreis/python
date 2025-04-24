import numpy as np

# Example coefficients from polyfit
coefficients = np.array([2.3142857142857136, 1.0476190476190468])  # Represents 2.2x + 1

# Convert to polynomial equation format
poly_eq = np.poly1d(coefficients)

# Print the equation
print(poly_eq)