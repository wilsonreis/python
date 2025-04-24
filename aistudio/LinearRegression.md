Ótima ideia! Entender como as coisas funcionam "por baixo dos panos" é excelente para consolidar o conhecimento.

A `LinearRegression` do scikit-learn encontra os coeficientes (incluindo o intercepto) de uma equação linear que melhor se ajusta aos dados, minimizando a soma dos quadrados das diferenças entre os valores observados e os valores previstos pelo modelo. Isso é conhecido como **Mínimos Quadrados Ordinários (OLS - Ordinary Least Squares)**.

Para um modelo linear `y = b0 + b1*x1 + b2*x2 + ... + bn*xn`, podemos encontrar os coeficientes `b = [b0, b1, ..., bn]` usando a **Equação Normal**:

`b = (X_b^T * X_b)^(-1) * X_b^T * y`

Onde:
*   `y`: vetor dos valores da variável dependente.
*   `X_b`: matriz das variáveis independentes com uma coluna adicional de 1s (para representar o termo do intercepto `b0`).
*   `X_b^T`: transposta da matriz `X_b`.
*   `*`: multiplicação de matrizes.
*   `^(-1)`: inversa da matriz.

Vamos implementar isso em Python.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as SklearnLinearRegression # Para comparação

class MinhaRegressaoLinear:
    """
    Implementação simplificada da Regressão Linear usando a Equação Normal.
    """
    def __init__(self):
        """Inicializa o modelo. Os coeficientes serão armazenados após o treino."""
        self.coef_ = None      # Armazenará os coeficientes (b1, b2, ...)
        self.intercept_ = None # Armazenará o intercepto (b0)
        self._beta = None      # Armazenará o vetor completo de coeficientes [b0, b1, ...]

    def fit(self, X, y):
        """
        Ajusta o modelo linear aos dados de treino X e y.

        Args:
            X (np.ndarray): Array 2D (n_samples, n_features) das variáveis independentes.
            y (np.ndarray): Array 1D (n_samples,) da variável dependente.
        """
        # 1. Adicionar a coluna de 1s a X para o termo de intercepto (b0)
        #    np.ones((X.shape[0], 1)) cria uma coluna de 1s com o mesmo número de linhas que X
        #    np.c_ concatena colunas
        X_b = np.c_[np.ones((X.shape[0], 1)), X]

        # 2. Calcular os coeficientes usando a Equação Normal: beta = (X_b^T * X_b)^(-1) * X_b^T * y
        try:
            # Transposta de X_b: X_b.T
            # Multiplicação de matrizes: @ (ou np.dot)
            # Inversa da matriz: np.linalg.inv()
            parte1 = np.linalg.inv(X_b.T @ X_b)
            parte2 = X_b.T @ y
            self._beta = parte1 @ parte2
        except np.linalg.LinAlgError:
            # A inversa pode não existir se as colunas de X forem linearmente dependentes
            # Scikit-learn usa métodos mais robustos (como SVD) para lidar com isso.
            # Aqui, vamos usar a pseudo-inversa como alternativa simples.
            print("Aviso: A matriz (X_b.T @ X_b) é singular. Usando pseudo-inversa.")
            self._beta = np.linalg.pinv(X_b.T @ X_b) @ (X_b.T @ y)


        # 3. Separar o intercepto (primeiro elemento de beta) dos outros coeficientes
        self.intercept_ = self._beta[0]
        self.coef_ = self._beta[1:]

        print(f"Modelo treinado com sucesso!")
        print(f"Intercepto (b0): {self.intercept_}")
        print(f"Coeficientes (b1, b2, ...): {self.coef_}")

    def predict(self, X):
        """
        Realiza previsões usando o modelo linear treinado.

        Args:
            X (np.ndarray): Array 2D (n_samples, n_features) das variáveis independentes
                            para as quais fazer previsões.

        Returns:
            np.ndarray: Array 1D (n_samples,) com os valores previstos.
        """
        if self._beta is None:
            raise Exception("O modelo precisa ser treinado antes de fazer previsões. Chame o método fit().")

        # 1. Adicionar a coluna de 1s a X
        X_b = np.c_[np.ones((X.shape[0], 1)), X]

        # 2. Calcular as previsões: y_pred = X_b * beta
        y_pred = X_b @ self._beta
        return y_pred

# --- Aplicação de Exemplo ---

print("--- Gerando Dados Sintéticos ---")
# Vamos criar dados sintéticos onde y tem uma relação linear com X mais algum ruído
np.random.seed(42) # Para reprodutibilidade
n_samples = 100
X = 2 * np.random.rand(n_samples, 1) # Uma variável independente
# Relação real: y = 4 + 3*X + ruído gaussiano
y_real = 4 + 3 * X
noise = np.random.randn(n_samples, 1) # Ruído
y = y_real + noise
y = y.ravel() # Transforma y em um array 1D, como esperado pelo fit

print(f"Shape de X: {X.shape}")
print(f"Shape de y: {y.shape}")

# Visualizar os dados gerados
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.7, label='Dados Gerados')
plt.plot(X, y_real, color='gray', linestyle='--', label='Relação Real (y = 4 + 3x)')
plt.xlabel("Variável Independente (X)")
plt.ylabel("Variável Dependente (y)")
plt.title("Dados Sintéticos para Regressão Linear")
plt.legend()
plt.grid(True)
# plt.show() # Descomente se quiser ver o gráfico agora

print("\n--- Treinando Nosso Modelo (MinhaRegressaoLinear) ---")
meu_modelo = MinhaRegressaoLinear()
meu_modelo.fit(X, y)

print("\n--- Treinando Modelo do Scikit-learn para Comparação ---")
sk_modelo = SklearnLinearRegression()
sk_modelo.fit(X, y)
print(f"Intercepto (scikit-learn): {sk_modelo.intercept_}")
print(f"Coeficientes (scikit-learn): {sk_modelo.coef_}")

# Comparando os resultados (devem ser muito próximos)
assert np.allclose(meu_modelo.intercept_, sk_modelo.intercept_), "Interceptos diferem!"
assert np.allclose(meu_modelo.coef_, sk_modelo.coef_), "Coeficientes diferem!"
print("\nOs resultados do nosso modelo e do scikit-learn são consistentes!")

print("\n--- Fazendo Previsões ---")
# Criando novos dados para prever
X_new = np.array([[0], [1.0], [2.0]]) # Valores de X = 0, 1.0 e 2.0
print(f"Novos dados (X_new):\n{X_new}")

y_pred_meu = meu_modelo.predict(X_new)
y_pred_sk = sk_modelo.predict(X_new)

print(f"\nPrevisões (Nosso Modelo): {y_pred_meu}")
print(f"Previsões (Scikit-learn): {y_pred_sk}")

# Adicionar a linha de regressão do nosso modelo ao gráfico
plt.plot(X_new, y_pred_meu, "r-", linewidth=2, label="Linha de Regressão (Nosso Modelo)")
plt.legend()
plt.show() # Mostrar o gráfico final com a linha de regressão

print("\n--- Exemplo com Múltiplas Variáveis ---")
# Gerar dados com 2 variáveis independentes
X_multi = 2 * np.random.rand(n_samples, 2) # Agora com 2 colunas
# Relação real: y = 4 + 3*x1 + 5*x2 + ruído
y_multi_real = 4 + 3 * X_multi[:, 0] + 5 * X_multi[:, 1]
noise_multi = np.random.randn(n_samples)
y_multi = y_multi_real + noise_multi

print(f"Shape de X_multi: {X_multi.shape}")
print(f"Shape de y_multi: {y_multi.shape}")

print("\n--- Treinando Nosso Modelo (Múltiplas Variáveis) ---")
meu_modelo_multi = MinhaRegressaoLinear()
meu_modelo_multi.fit(X_multi, y_multi)

print("\n--- Treinando Modelo Scikit-learn (Múltiplas Variáveis) ---")
sk_modelo_multi = SklearnLinearRegression()
sk_modelo_multi.fit(X_multi, y_multi)
print(f"Intercepto (scikit-learn): {sk_modelo_multi.intercept_}")
print(f"Coeficientes (scikit-learn): {sk_modelo_multi.coef_}")

# Comparando novamente
assert np.allclose(meu_modelo_multi.intercept_, sk_modelo_multi.intercept_), "Interceptos (multi) diferem!"
assert np.allclose(meu_modelo_multi.coef_, sk_modelo_multi.coef_), "Coeficientes (multi) diferem!"
print("\nOs resultados para múltiplas variáveis também são consistentes!")
```

**Explicação do Código:**

1.  **`MinhaRegressaoLinear` Classe:**
    *   `__init__`: Apenas inicializa os atributos `coef_`, `intercept_`, e `_beta` como `None`. Eles serão preenchidos após o treino.
    *   `fit(X, y)`:
        *   Adiciona uma coluna de `1`s à matriz `X` para criar `X_b`. Isso é essencial para que a multiplicação de matrizes calcule o termo de intercepto `b0` junto com os outros coeficientes.
        *   Calcula os coeficientes `_beta` usando a fórmula da Equação Normal: `np.linalg.inv(X_b.T @ X_b) @ (X_b.T @ y)`. Usamos `@` para multiplicação de matrizes e `np.linalg.inv` para a inversa.
        *   Incluí um `try-except` para usar a pseudo-inversa (`np.linalg.pinv`) caso a matriz `(X_b.T @ X_b)` seja singular (não invertível), o que pode acontecer se houver colinearidade perfeita entre as variáveis. Scikit-learn usa métodos mais sofisticados como Decomposição de Valor Singular (SVD) internamente, que são numericamente mais estáveis.
        *   Separa o primeiro valor de `_beta` (que corresponde à coluna de `1`s) como `intercept_` e o restante como `coef_`.
    *   `predict(X)`:
        *   Verifica se o modelo já foi treinado (se `_beta` não é `None`).
        *   Adiciona a coluna de `1`s aos novos dados `X`.
        *   Calcula as previsões multiplicando a matriz `X_b` (dos novos dados) pelo vetor de coeficientes `_beta` que foi aprendido no `fit`.

2.  **Aplicação de Exemplo:**
    *   **Dados Sintéticos:** Geramos dados `X` e `y` com uma relação linear conhecida (`y = 4 + 3x`) mais um ruído aleatório para simular dados reais.
    *   **Treinamento:** Instanciamos e treinamos tanto `MinhaRegressaoLinear` quanto `SklearnLinearRegression` com os mesmos dados.
    *   **Comparação:** Comparamos os `intercept_` e `coef_` encontrados pelos dois modelos. Eles devem ser praticamente idênticos (dentro da precisão de ponto flutuante).
    *   **Previsão:** Usamos ambos os modelos treinados para prever valores para novos dados `X_new`.
    *   **Visualização:** Plotamos os dados originais, a linha da relação real (se conhecida) e a linha de regressão encontrada pelo nosso modelo.
    *   **Múltiplas Variáveis:** Repetimos o processo com dados que têm duas variáveis independentes para mostrar que a implementação funciona para regressão linear múltipla também.

**Limitações e Diferenças do Scikit-learn:**

*   **Estabilidade Numérica:** A Equação Normal pode ser numericamente instável, especialmente se a matriz `(X_b^T * X_b)` estiver mal condicionada (próxima de singular) ou se o número de features for muito grande. O `LinearRegression` do Scikit-learn usa decomposição SVD, que é mais robusta.
*   **Eficiência:** Para um número muito grande de features, calcular a inversa da matriz pode ser computacionalmente caro (`O(n^3)`, onde `n` é o número de features). Métodos baseados em Gradiente Descendente (usados em `SGDRegressor` do scikit-learn) podem ser mais eficientes nesses casos. Para um número grande de amostras, a Equação Normal pode ser mais rápida que o Gradiente Descendente.
*   **Funcionalidades:** O Scikit-learn oferece muito mais, como opções de normalização de dados, tratamento de dados esparsos, regularização (Ridge, Lasso), etc.

Esta implementação simplificada, no entanto, captura a essência matemática do ajuste por Mínimos Quadrados Ordinários usando a Equação Normal, que é o fundamento por trás do `LinearRegression` do scikit-learn para conjuntos de dados onde essa abordagem é viável.