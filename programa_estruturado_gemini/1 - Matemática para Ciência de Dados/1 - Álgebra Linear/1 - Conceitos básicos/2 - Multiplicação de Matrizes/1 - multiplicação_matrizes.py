import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

resultado = np.matmul(A, B)  # Ou simplesmente A @ B
print(resultado)

print("---------------------------------------------------")
A = np.array([1, 2, 3, 4])
B = np.array([[5], [6], [7], [8]])
print("A", A)
print("B", B)
print("Tipo de B:", type(B))
print("Dimensões de b:", B.shape)

resultado = np.matmul(A, B)
print(resultado)
print("---------------------------------------------------")

'''
**Observações Importantes:**

*   **`np.matmul()` ou `@`:** Em NumPy, você pode usar `np.matmul(A, B)` ou o operador `@` (a partir do Python 3.5) para realizar a multiplicação de matrizes.
*   **`np.dot()`:**  Enquanto `np.dot()` também pode ser usado para multiplicação de matrizes em alguns casos, `np.matmul()` é geralmente preferível porque tem um comportamento mais consistente e previsível, especialmente com matrizes de dimensões maiores.
*   **Ordem é Importante:** A multiplicação de matrizes não é comutativa (A * B  ≠ B * A). A ordem das matrizes na multiplicação é crucial.
*   **Erros de Dimensão:** Se você tentar multiplicar matrizes incompatíveis, NumPy lançará um erro.
'''