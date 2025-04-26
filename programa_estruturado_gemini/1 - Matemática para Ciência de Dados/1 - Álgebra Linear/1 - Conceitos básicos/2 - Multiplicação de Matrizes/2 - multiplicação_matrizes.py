'''
A = | 1  2  3  4 |
    | 5  6  7  8 |
    | 9 10 11 12 |

B = | 13 14 |
    | 15 16 |
    | 17 18 |
    | 19 20 |
    
Dimensões: A é 3x4, B é 4x2. Resultado será uma matriz 3x2.

Cálculo (parcial, para ilustrar):

O elemento na primeira linha e primeira coluna do resultado seria:

(1*13 + 2*15 + 3*17 + 4*19) = (13 + 30 + 51 + 76) = 170    
'''


import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B = np.array([[13, 14], [15, 16], [17, 18], [19, 20]])

print("Dimensões de A:", A.shape)

print("Dimensões de b:", B.shape)




resultado = np.matmul(A, B)

print("resultado:", resultado)
print("Dimensões de resultado:", resultado.shape)

'''
**Observações Importantes:**

*   **`np.matmul()` ou `@`:** Em NumPy, você pode usar `np.matmul(A, B)` ou o operador `@` (a partir do Python 3.5) para realizar a multiplicação de matrizes.
*   **`np.dot()`:**  Enquanto `np.dot()` também pode ser usado para multiplicação de matrizes em alguns casos, `np.matmul()` é geralmente preferível porque tem um comportamento mais consistente e previsível, especialmente com matrizes de dimensões maiores.
*   **Ordem é Importante:** A multiplicação de matrizes não é comutativa (A * B  ≠ B * A). A ordem das matrizes na multiplicação é crucial.
*   **Erros de Dimensão:** Se você tentar multiplicar matrizes incompatíveis, NumPy lançará um erro.
'''