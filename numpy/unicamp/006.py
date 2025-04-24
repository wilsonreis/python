import biblioteca as bib
import numpy as np


# Defina as matrizes A e B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Multiplique as matrizes A e B
C = np.dot(A, B)

# Imprima a matriz resultante
print(C)