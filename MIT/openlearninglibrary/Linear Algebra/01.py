import numpy as np
#x + 3y = 1
#2x − y = −2
# Defina a matriz de coeficientes
A = np.array([[1, 3], [2, -1]])

# Defina o vetor de constantes
b = np.array([1, -2])

# Resolva o sistema de equações lineares
x = np.linalg.solve(A, b)

print("A solução do sistema de equações lineares é:")
print("x =", x[0])
print("y =", x[1])