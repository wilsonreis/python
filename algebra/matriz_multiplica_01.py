# Importe a biblioteca numpy para trabalhar com matrizes
import numpy as np

# Construa a matriz A de 3x2
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Construa a matriz B de 3x2
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Imprima as matrizes A e B
print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

# Multiplique as matrizes A e B
C = np.dot(A, B.T)

# Imprima o resultado da multiplicação
print("\nResultado da multiplicação:")
print(C)