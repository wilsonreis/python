Okay, vamos criar e detalhar uma função em Python para o Método de Eliminação de Gauss.

**Conceito do Método de Eliminação de Gauss**

A Eliminação de Gauss é um algoritmo fundamental da álgebra linear usado para:

1.  **Resolver sistemas de equações lineares:** `Ax = b`
2.  **Encontrar a matriz inversa:** `A⁻¹`
3.  **Calcular o determinante de uma matriz:** `det(A)`
4.  **Determinar o posto (rank) de uma matriz.**

O método funciona transformando a matriz aumentada `[A | b]` do sistema em uma **matriz triangular superior** (ou forma escalonada por linhas) através de operações elementares nas linhas. Após obter a forma triangular superior, o sistema pode ser resolvido facilmente por **substituição reversa (ou retro-substituição)**.

**Operações Elementares de Linha:**

1.  **Troca:** Trocar duas linhas de posição.
2.  **Escalonamento:** Multiplicar uma linha por uma constante não nula.
3.  **Combinação Linear:** Somar a uma linha um múltiplo de outra linha.

**Passos Principais:**

1.  **Fase de Eliminação (Forward Elimination):**
    *   Transformar a matriz aumentada `[A | b]` em uma forma escalonada por linhas (idealmente triangular superior).
    *   Para cada coluna `k` (começando da primeira):
        *   **Pivoteamento (Opcional, mas recomendado para estabilidade numérica):** Encontrar a linha `i >= k` com o maior valor absoluto na coluna `k`. Trocar a linha `k` com essa linha `i`. Isso ajuda a evitar divisão por números pequenos ou zero. (Usaremos *pivoteamento parcial*).
        *   Se o pivô `A[k][k]` for zero (ou muito próximo de zero) mesmo após o pivoteamento, a matriz é singular (pode não ter solução única).
        *   Para cada linha `i` abaixo da linha do pivô (`i > k`): Calcular o multiplicador `m = A[i][k] / A[k][k]`. Subtrair `m` vezes a linha do pivô (`k`) da linha `i` (`Linha[i] = Linha[i] - m * Linha[k]`). Isso zera os elementos abaixo do pivô na coluna `k`.
2.  **Verificação de Solução:**
    *   Após a eliminação, verificar se o sistema é:
        *   **Inconsistente (sem solução):** Se alguma linha tiver a forma `[0, 0, ..., 0 | c]` onde `c` é não nulo.
        *   **Possível Indeterminado (infinitas soluções):** Se houver menos pivôs não nulos do que variáveis (linhas de zeros `[0, 0, ..., 0 | 0]`) e não for inconsistente.
        *   **Possível Determinado (solução única):** Se o número de pivôs não nulos for igual ao número de variáveis e não for inconsistente.
3.  **Fase de Substituição Reversa (Back Substitution):**
    *   Se houver solução única, resolver o sistema triangular superior começando pela última equação e substituindo os valores encontrados nas equações anteriores.
    *   `x[n-1] = b[n-1] / A[n-1][n-1]`
    *   `x[n-2] = (b[n-2] - A[n-2][n-1]*x[n-1]) / A[n-2][n-2]`
    *   ... e assim por diante até `x[0]`.

**Implementação em Python**

```python
import copy

def eliminacao_gauss(matriz_aumentada_original):
    """
    Resolve um sistema de equações lineares Ax = b usando o Método de Eliminação de Gauss
    com pivoteamento parcial.

    Argumentos:
        matriz_aumentada_original (list[list[float]]): A matriz aumentada [A | b]
                                                        onde A é a matriz de coeficientes e
                                                        b é o vetor de termos constantes.

    Retorna:
        list[float]: Uma lista contendo a solução única [x1, x2, ..., xn] se existir.
        None: Se o sistema for inconsistente (sem solução) ou
              possível indeterminado (infinitas soluções). Imprime uma mensagem indicando o caso.

    Observação:
        A função trabalha com uma cópia da matriz original para não modificá-la.
        Utiliza uma pequena tolerância (epsilon) para comparações com zero devido
        às imprecisões de ponto flutuante.
    """
    # --- Validação de Entrada e Inicialização ---
    if not matriz_aumentada_original:
        print("Erro: Matriz de entrada está vazia.")
        return None

    n = len(matriz_aumentada_original)  # Número de equações (linhas)
    try:
        m = len(matriz_aumentada_original[0]) # Número total de colunas
    except IndexError:
        print("Erro: Linhas da matriz estão vazias.")
        return None

    if m != n + 1:
        print(f"Erro: A matriz aumentada deve ter N linhas e N+1 colunas. Recebido {n}x{m}.")
        return None

    # Cria uma cópia profunda para não modificar a matriz original
    matriz = copy.deepcopy(matriz_aumentada_original)
    epsilon = 1e-10 # Tolerância para comparação com zero

    # --- Fase 1: Eliminação Progressiva (Forward Elimination) ---
    print("\n--- Iniciando Eliminação de Gauss ---")
    print("Matriz Original:")
    for linha in matriz:
        print([round(elem, 5) for elem in linha])

    for k in range(n): # k é a coluna do pivô atual (e a linha)
        # Pivoteamento Parcial: Encontrar a linha com o maior pivô em módulo
        indice_max = k
        for i in range(k + 1, n):
            if abs(matriz[i][k]) > abs(matriz[indice_max][k]):
                indice_max = i

        # Trocar linha k com linha indice_max
        if indice_max != k:
            print(f"\nPivoteamento: Trocando linha {k+1} com linha {indice_max+1}")
            matriz[k], matriz[indice_max] = matriz[indice_max], matriz[k]
            print("Matriz após troca:")
            for linha in matriz:
                print([round(elem, 5) for elem in linha])

        # Verificar se o pivô é muito pequeno (próximo de zero)
        pivo = matriz[k][k]
        if abs(pivo) < epsilon:
            # Não é possível usar este pivô. Isso pode indicar que a matriz
            # é singular (sem solução única). Continuamos a eliminação,
            # a verificação final determinará o tipo de solução.
            print(f"\nAtenção: Pivô na coluna {k+1} é próximo de zero ({pivo:.2e}).")
            continue # Pula para a próxima coluna k

        # Eliminação: Zerar os elementos abaixo do pivô na coluna k
        print(f"\nEliminando abaixo do pivô na coluna {k+1} (Linha {k+1})")
        for i in range(k + 1, n): # Para cada linha i abaixo da linha do pivô k
            fator = matriz[i][k] / pivo
            print(f"  L{i+1} = L{i+1} - ({fator:.4f}) * L{k+1}")
            # Atualizar toda a linha i
            for j in range(k, m): # Começa da coluna k, pois as anteriores já são zero
                matriz[i][j] = matriz[i][j] - fator * matriz[k][j]
            # Opcional: Forçar o elemento a ser zero para evitar erros de ponto flutuante
            # matriz[i][k] = 0.0

        print("Matriz após eliminação parcial:")
        for linha in matriz:
            print([round(elem, 5) for elem in linha])

    print("\n--- Fim da Fase de Eliminação ---")
    print("Matriz Escalonada (Triangular Superior):")
    for linha in matriz:
        print([round(elem, 5) for elem in linha])

    # --- Fase 2: Verificação do Tipo de Solução ---
    # Verificar inconsistências (linha [0 0 ... 0 | c] com c != 0)
    # Verificar dependência linear (linha [0 0 ... 0 | 0])
    rank = 0
    inconsistente = False
    for i in range(n):
        # Verifica se a parte dos coeficientes da linha é toda zero (ou quase zero)
        coeficientes_zero = all(abs(matriz[i][j]) < epsilon for j in range(n))

        if coeficientes_zero:
            # Se os coeficientes são zero, verifica o termo constante
            if abs(matriz[i][n]) > epsilon: # matriz[i][n] é o elemento b[i]
                print(f"\nSistema Inconsistente: Linha {i+1} é [0 ... 0 | {matriz[i][n]:.4f}] (não nulo).")
                print("O sistema não possui solução.")
                inconsistente = True
                break
            # else: Linha [0 ... 0 | 0] indica dependência, não inconsistência.
        else:
            rank += 1 # Conta como uma linha efetiva (não nula na parte A)

    if inconsistente:
        return None

    if rank < n:
        print(f"\nSistema Possível Indeterminado: Posto ({rank}) < Número de variáveis ({n}).")
        print("O sistema possui infinitas soluções.")
        return None

    # Se chegou aqui, rank == n, o sistema tem solução única.

    # --- Fase 3: Substituição Reversa (Back Substitution) ---
    print("\n--- Iniciando Substituição Reversa ---")
    x = [0.0] * n # Inicializa o vetor solução

    # Começa da última equação (linha n-1) até a primeira (linha 0)
    for i in range(n - 1, -1, -1):
        # Calcula a soma dos termos A[i][j] * x[j] para j > i
        soma = 0.0
        for j in range(i + 1, n):
            soma += matriz[i][j] * x[j]

        # Calcula x[i]
        # O pivô matriz[i][i] não deve ser zero aqui, pois verificamos rank == n
        pivo_i = matriz[i][i]
        if abs(pivo_i) < epsilon:
             # Segurança extra, embora não devesse ocorrer se as verificações anteriores estiverem corretas.
             print(f"Erro inesperado: Pivô zero encontrado na substituição reversa na linha {i+1}, coluna {i+1}")
             print("Isso pode indicar um problema numérico ou um erro na lógica de verificação.")
             return None # Ou lançar uma exceção

        x[i] = (matriz[i][n] - soma) / pivo_i
        print(f"  x[{i+1}] = ({matriz[i][n]:.4f} - {soma:.4f}) / {pivo_i:.4f} = {x[i]:.4f}")

    print("\n--- Fim da Substituição Reversa ---")
    return x

# --- Exemplos de Uso ---

# Exemplo 1: Sistema com Solução Única
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
matriz1 = [
    [2,  1, -1,   8],
    [-3, -1,  2, -11],
    [-2,  1,  2,  -3]
]
solucao1 = eliminacao_gauss(matriz1)
if solucao1:
    print(f"\nSolução Única encontrada: x = {[round(val, 5) for val in solucao1]}") # Esperado: [2, 3, -1]

print("\n" + "="*50 + "\n")

# Exemplo 2: Sistema Inconsistente (Sem Solução)
# x + y + z = 1
# x + y + z = 2  <- Equação inconsistente com a primeira
# 2x + y - z = 3
matriz2 = [
    [1, 1, 1, 1],
    [1, 1, 1, 2],
    [2, 1, -1, 3]
]
solucao2 = eliminacao_gauss(matriz2)
if solucao2 is None:
    print("\nConforme esperado, o sistema não teve solução ou teve infinitas soluções.")

print("\n" + "="*50 + "\n")

# Exemplo 3: Sistema Possível Indeterminado (Infinitas Soluções)
# x + y + z = 3
# 2x + 2y + 2z = 6  <- Equação dependente da primeira
# x + 2y + 3z = 4
matriz3 = [
    [1, 1, 1, 3],
    [2, 2, 2, 6],
    [1, 2, 3, 4]
]
solucao3 = eliminacao_gauss(matriz3)
if solucao3 is None:
    print("\nConforme esperado, o sistema não teve solução única.")

print("\n" + "="*50 + "\n")

# Exemplo 4: Sistema com Pivô Zero inicial (requer troca de linha)
# 0x + y + z = 5
# x + 0y - z = 1
# x + y + 0z = 4
matriz4 = [
    [0, 1, 1, 5],
    [1, 0, -1, 1],
    [1, 1, 0, 4]
]
solucao4 = eliminacao_gauss(matriz4)
if solucao4:
    print(f"\nSolução Única encontrada: x = {[round(val, 5) for val in solucao4]}") # Esperado: [2, 2, 3] (Verificar: 0+2+3=5 ok; 2-3= -1 != 1 Erro no meu cálculo manual ou exemplo. Vamos conferir.
# Verificação exemplo 4:
# Se x=2, y=2, z=3:
# Eq1: 0*2 + 1*2 + 1*3 = 2 + 3 = 5 (OK)
# Eq2: 1*2 + 0*2 - 1*3 = 2 - 3 = -1 (OK) -> O exemplo original no comentário estava errado. Correto é -1.
# Eq3: 1*2 + 1*2 + 0*3 = 2 + 2 = 4 (OK)
# O código deve achar x=[2, 2, 3] se o b[1] for -1. Vamos corrigir a matriz de exemplo 4:
matriz4_corrigida = [
    [0, 1, 1, 5],
    [1, 0, -1, -1], # Corrigido para -1
    [1, 1, 0, 4]
]
print("\nExemplo 4 (Corrigido):")
solucao4_corrigida = eliminacao_gauss(matriz4_corrigida)
if solucao4_corrigida:
    print(f"\nSolução Única encontrada: x = {[round(val, 5) for val in solucao4_corrigida]}") # Esperado: [2, 2, 3]

```

**Detalhamento do Código:**

1.  **Import `copy`:** Necessário para usar `copy.deepcopy()`, que cria uma cópia independente da matriz original, garantindo que a matriz passada como argumento não seja alterada.
2.  **Assinatura da Função:** `eliminacao_gauss(matriz_aumentada_original)` recebe a matriz aumentada como uma lista de listas.
3.  **Docstring:** Explica o propósito da função, argumentos, o que ela retorna e observações importantes.
4.  **Validação de Entrada:** Verifica se a matriz não está vazia e se tem o formato correto (N linhas e N+1 colunas).
5.  **Cópia da Matriz:** `matriz = copy.deepcopy(matriz_aumentada_original)` garante que as operações sejam feitas em uma cópia.
6.  **`epsilon`:** Uma tolerância pequena (`1e-10`) é definida para comparar números de ponto flutuante com zero. Isso é crucial porque operações aritméticas podem resultar em valores muito pequenos (como `1e-15`) que deveriam ser zero.
7.  **Fase de Eliminação (Loop `k`):**
    *   Itera pelas colunas de `0` a `n-1`, onde `n` é o número de equações/variáveis. `k` representa a coluna e a linha do pivô atual.
    *   **Pivoteamento Parcial:**
        *   Encontra o índice (`indice_max`) da linha (a partir de `k`) que contém o maior valor absoluto na coluna `k`.
        *   Se `indice_max` for diferente de `k`, troca a linha `k` pela linha `indice_max` usando atribuição múltipla (`matriz[k], matriz[indice_max] = matriz[indice_max], matriz[k]`). Isso coloca o maior pivô possível na posição diagonal `matriz[k][k]`.
        *   Imprime mensagens informativas sobre a troca.
    *   **Verificação do Pivô:** Verifica se o elemento pivô `matriz[k][k]` é muito próximo de zero (`abs(pivo) < epsilon`). Se for, imprime um aviso e continua para a próxima coluna (`k+1`). O sistema pode ser singular, mas a decisão final é feita após a eliminação completa.
    *   **Eliminação (Loop `i`):**
        *   Itera pelas linhas `i` abaixo da linha do pivô (`k+1` até `n-1`).
        *   Calcula o `fator = matriz[i][k] / pivo`.
        *   Atualiza cada elemento `matriz[i][j]` na linha `i` (a partir da coluna `k`, pois as colunas anteriores já foram zeradas em passos anteriores) subtraindo `fator * matriz[k][j]`.
        *   Imprime mensagens sobre a operação `Li = Li - fator * Lk`.
    *   Imprime a matriz após cada etapa de eliminação para visualização.
8.  **Verificação do Tipo de Solução:**
    *   Após a eliminação, a matriz está (ou deveria estar) em forma escalonada.
    *   Itera pelas linhas da matriz escalonada.
    *   Para cada linha `i`, verifica se todos os coeficientes (`matriz[i][j]` para `j < n`) são próximos de zero.
    *   Se os coeficientes são zero:
        *   Verifica o termo constante `matriz[i][n]`. Se for diferente de zero (`> epsilon`), a linha representa `0 = c` (onde `c != 0`), indicando um **Sistema Inconsistente**. A flag `inconsistente` é setada e o loop quebra.
        *   Se o termo constante também for zero, a linha é `[0 ... 0 | 0]`, indicando dependência linear.
    *   Se os coeficientes não são todos zero, incrementa o `rank` (posto da matriz de coeficientes).
    *   Após o loop:
        *   Se `inconsistente` for `True`, imprime a mensagem e retorna `None`.
        *   Se `rank < n` (e não é inconsistente), significa que há menos equações linearmente independentes do que variáveis, resultando em **Infinitas Soluções (Sistema Possível Indeterminado)**. Imprime a mensagem e retorna `None`.
9.  **Fase de Substituição Reversa:**
    *   Executada apenas se `rank == n` (solução única).
    *   Cria um vetor `x` de tamanho `n` inicializado com zeros.
    *   Itera pelas linhas de baixo para cima (`range(n - 1, -1, -1)`).
    *   Para cada linha `i`:
        *   Calcula a `soma` dos termos `matriz[i][j] * x[j]` para `j` maior que `i` (usando os valores de `x` já calculados).
        *   Calcula `x[i]` usando a fórmula: `x[i] = (matriz[i][n] - soma) / matriz[i][i]`. O pivô `matriz[i][i]` não deve ser zero neste ponto se `rank == n`. Uma verificação extra de segurança contra divisão por zero é incluída.
        *   Imprime o cálculo de cada `x[i]`.
    *   Retorna o vetor solução `x`.
10. **Exemplos:** Demonstram como usar a função com diferentes tipos de sistemas.

Esta implementação é robusta pois inclui pivoteamento parcial (melhora a estabilidade numérica) e verifica explicitamente os casos de solução única, sem solução e infinitas soluções. As impressões detalhadas ajudam a entender o processo passo a passo.