Com certeza! Vamos explorar a multiplicação de matrizes não quadráticas com exemplos matemáticos e implementações em Python usando NumPy.

**Conceitos Fundamentais**

*   **Dimensões:** Uma matriz é descrita por suas dimensões (linhas x colunas). Uma matriz *m x n* tem *m* linhas e *n* colunas.
*   **Compatibilidade:** Para multiplicar duas matrizes, a seguinte condição deve ser atendida: o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.
*   **Resultado:** Se você multiplicar uma matriz *m x n* por uma matriz *n x p*, o resultado será uma matriz *m x p*.

**Exemplos Matemáticos e Código Python**

**Exemplo 1: Multiplicando uma Matriz 2x3 por uma Matriz 3x2**

*   **Matrizes:**

    ```
    A = | 1  2  3 |
        | 4  5  6 |

    B = | 7  8 |
        | 9  10 |
        | 11 12 |
    ```

*   **Dimensões:** A é 2x3, B é 3x2. A multiplicação é possível porque o número de colunas de A (3) é igual ao número de linhas de B (3). O resultado será uma matriz 2x2.

*   **Cálculo:**

    ```
    Resultado = | (1*7 + 2*9 + 3*11)  (1*8 + 2*10 + 3*12) |
                | (4*7 + 5*9 + 6*11)  (4*8 + 5*10 + 6*12) |

              = | (7 + 18 + 33)  (8 + 20 + 36) |
                | (28 + 45 + 66) (32 + 50 + 72) |

              = | 58  64 |
                | 139 154 |
    ```

*   **Código Python (NumPy):**

    ```python
    import numpy as np

    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])

    resultado = np.matmul(A, B)  # Ou simplesmente A @ B

    print(resultado)
    # Saída:
    # [[ 58  64]
    #  [139 154]]
    ```

**Exemplo 2: Multiplicando uma Matriz 1x4 por uma Matriz 4x1**

*   **Matrizes:**

    ```
    A = | 1  2  3  4 |

    B = | 5 |
        | 6 |
        | 7 |
        | 8 |
    ```

*   **Dimensões:** A é 1x4, B é 4x1. Resultado será uma matriz 1x1 (um escalar).

*   **Cálculo:**

    ```
    Resultado = | (1*5 + 2*6 + 3*7 + 4*8) |
              = | (5 + 12 + 21 + 32) |
              = | 70 |
    ```

*   **Código Python:**

    ```python
    import numpy as np

    A = np.array([[1, 2, 3, 4]])
    B = np.array([[5], [6], [7], [8]])

    resultado = np.matmul(A, B)

    print(resultado)
    # Saída:
    # [[70]]
    ```

**Exemplo 3: Multiplicando uma Matriz 3x4 por uma Matriz 4x2**

*   **Matrizes:**

    ```
    A = | 1  2  3  4 |
        | 5  6  7  8 |
        | 9 10 11 12 |

    B = | 13 14 |
        | 15 16 |
        | 17 18 |
        | 19 20 |
    ```

*   **Dimensões:** A é 3x4, B é 4x2. Resultado será uma matriz 3x2.

*   **Cálculo (parcial, para ilustrar):**

    O elemento na primeira linha e primeira coluna do resultado seria:

    `(1*13 + 2*15 + 3*17 + 4*19) = (13 + 30 + 51 + 76) = 170`

*   **Código Python:**

    ```python
    import numpy as np

    A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    B = np.array([[13, 14], [15, 16], [17, 18], [19, 20]])

    resultado = np.matmul(A, B)

    print(resultado)
    # Saída:
    # [[170 180]
    #  [394 416]
    #  [618 652]]
    ```

**Observações Importantes:**

*   **`np.matmul()` ou `@`:** Em NumPy, você pode usar `np.matmul(A, B)` ou o operador `@` (a partir do Python 3.5) para realizar a multiplicação de matrizes.
*   **`np.dot()`:**  Enquanto `np.dot()` também pode ser usado para multiplicação de matrizes em alguns casos, `np.matmul()` é geralmente preferível porque tem um comportamento mais consistente e previsível, especialmente com matrizes de dimensões maiores.
*   **Ordem é Importante:** A multiplicação de matrizes não é comutativa (A * B  ≠ B * A). A ordem das matrizes na multiplicação é crucial.
*   **Erros de Dimensão:** Se você tentar multiplicar matrizes incompatíveis, NumPy lançará um erro.
