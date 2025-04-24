# prompt: explique como é feita a multiplicação de matriz por matriz

A multiplicação de matrizes não é uma operação elemento a elemento como a soma ou subtração.  Ela envolve um processo mais complexo que resulta em uma nova matriz com um número de linhas igual ao da primeira matriz e um número de colunas igual ao da segunda matriz.  A condição fundamental para a multiplicação é que o número de colunas da primeira matriz seja igual ao número de linhas da segunda.

**Passo a passo:**

1. **Compatibilidade:**  Verifica-se se as matrizes são compatíveis para multiplicação. Se a matriz A tem dimensões *m x n* (m linhas e n colunas) e a matriz B tem dimensões *n x p*, então a multiplicação A x B é possível, e a matriz resultante C terá dimensões *m x p*. Se o número de colunas de A for diferente do número de linhas de B, a multiplicação não é possível.


2. **Cálculo de cada elemento da matriz resultante:** Cada elemento *c<sub>ij</sub>* da matriz resultante C é calculado como a soma dos produtos dos elementos correspondentes da i-ésima linha de A e da j-ésima coluna de B.  Mais precisamente:

   *c<sub>ij</sub> = Σ (a<sub>ik</sub> * b<sub>kj</sub>)*, onde k varia de 1 a n (o número de colunas de A e o número de linhas de B).

**Exemplo:**

Vamos considerar as matrizes A (2x3) e B (3x2):

A = | 1  2  3 |
    | 4  5  6 |

B = | 7  8 |
    | 9  10|
    |11  12|

Para calcular o elemento *c<sub>11</sub>* da matriz resultante C (que será 2x2), fazemos:

*c<sub>11</sub> = (1*7) + (2*9) + (3*11) = 7 + 18 + 33 = 58*

Seguindo o mesmo processo para os demais elementos:

*c<sub>12</sub> = (1*8) + (2*10) + (3*12) = 8 + 20 + 36 = 64*
*c<sub>21</sub> = (4*7) + (5*9) + (6*11) = 28 + 45 + 66 = 139*
*c<sub>22</sub> = (4*8) + (5*10) + (6*12) = 32 + 50 + 72 = 154*

Portanto, a matriz resultante C é:

C = | 58  64 |
    | 139 154|


**Em resumo:** A multiplicação de matrizes é uma operação que envolve a soma de produtos de linhas e colunas, e a ordem das matrizes importa (A x B ≠ B x A, geralmente). A compatibilidade entre as dimensões é fundamental para que a operação seja definida.
