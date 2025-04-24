#x - y + z = 6
#2y + 3z = 8
#4z = 8
import numpy as np

# Defina a matriz de coeficientes
A = np.array([[1, -1, 1], [0, 2, 3], [0, 0, 4]])

# Defina o vetor de constantes
b = np.array([6, 8, 8])

# Resolva o sistema de equações lineares
x = np.linalg.solve(A, b)

print("A solução do sistema de equações lineares é:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])