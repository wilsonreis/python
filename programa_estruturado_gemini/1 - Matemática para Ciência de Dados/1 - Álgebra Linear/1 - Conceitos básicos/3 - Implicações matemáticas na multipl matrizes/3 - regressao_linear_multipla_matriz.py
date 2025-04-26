import numpy as np
import pandas as pd  # Importe pandas se você quiser usar DataFrames

def regressao_linear_multipla_matriz(X, y):
    """
    Calcula os coeficientes de um modelo de regressão linear múltipla usando multiplicação de matrizes.

    Args:
        X (numpy.ndarray): Matriz de características (variáveis independentes).
                          Cada linha representa uma observação e cada coluna uma característica.
                          IMPORTANTE: A primeira coluna de X deve ser uma coluna de 1s (para o intercepto).
        y (numpy.ndarray): Vetor de variável dependente (a variável que você quer prever).

    Returns:
        numpy.ndarray: Vetor de coeficientes (incluindo o intercepto).
                       Retorna None se ocorrer um erro (por exemplo, matriz X não inversível).
    """
    try:
        # 1. Transposta de X
        X_transposta = X.T
        print("X_transposta:", X_transposta)
        # 2. Multiplicação de X transposta por X
        X_transposta_X = X_transposta @ X  # ou np.dot(X_transposta, X)
        print("X_transposta_X:", X_transposta_X)
        # 3. Inversa de (X'X)
        # Adiciona um regularizador (ridge regression) para lidar com multicolinearidade
        # Ajuste o valor de 'alpha' conforme necessário.  Valores pequenos já podem ajudar.
        alpha = 0.0001  # Pequeno valor para regularização
        I = np.identity(X_transposta_X.shape[0])  # Matriz identidade
        X_transposta_X_regularizado = X_transposta_X + alpha * I
        X_transposta_X_inversa = np.linalg.inv(X_transposta_X_regularizado)



        # 4. Multiplicação de X transposta por y
        X_transposta_y = X_transposta @ y  # ou np.dot(X_transposta, y)

        # 5. Coeficientes: b = (X'X)^-1 * X'y
        coeficientes = X_transposta_X_inversa @ X_transposta_y # ou np.dot(X_transposta_X_inversa, X_transposta_y)

        return coeficientes

    except np.linalg.LinAlgError:
        print("Erro: A matriz X'X não é inversível.  Isso pode acontecer se houver multicolinearidade perfeita ou se X não tiver posto completo.")
        return None  # Indica que a regressão falhou

# Exemplo de uso:
if __name__ == '__main__':
    # Criando dados de exemplo (substitua por seus próprios dados)
    # Vamos usar 3 variáveis independentes (características) e 5 observações
    X = np.array([
        [1, 2, 3, 4],  # Observação 1 (1 é para o intercepto)
        [1, 5, 6, 7],  # Observação 2
        [1, 8, 9, 10], # Observação 3
        [1, 11, 12, 13],# Observação 4
        [1, 14, 15, 16]  # Observação 5
    ])
    print("X:", X)
    y = np.array([10, 20, 30, 40, 50])  # Valores da variável dependente

    # Executando a regressão linear múltipla usando multiplicação de matrizes
    coeficientes_obtidos = regressao_linear_multipla_matriz(X, y)

    if coeficientes_obtidos is not None:
        print("Coeficientes obtidos:")
        print(coeficientes_obtidos)

        # Interpretando os resultados:
        # O primeiro coeficiente é o intercepto (o valor de y quando todas as variáveis independentes são 0).
        # Os coeficientes restantes representam o efeito de cada variável independente em y, mantendo as outras constantes.

        # Exemplo de predição para uma nova observação:
        nova_observacao = np.array([1, 17, 18, 19])  # Inclua o 1 para o intercepto
        predicao = nova_observacao @ coeficientes_obtidos # ou np.dot(nova_observacao, coeficientes_obtidos)
        print("\nPredição para a nova observação:", predicao)

    #Demonstrando o uso com Pandas DataFrame (opcional):
    """
    data = {'X1': [2, 5, 8, 11, 14],
            'X2': [3, 6, 9, 12, 15],
            'X3': [4, 7, 10, 13, 16],
            'y': [10, 20, 30, 40, 50]}

    df = pd.DataFrame(data)

    # Adicionar a coluna de 1s ao DataFrame para o intercepto
    df.insert(0, 'Intercept', 1)

    # Converter o DataFrame para numpy arrays
    X_df = df[['Intercept', 'X1', 'X2', 'X3']].values
    y_df = df['y'].values

    coeficientes_df = regressao_linear_multipla_matriz(X_df, y_df)

    if coeficientes_df is not None:
        print("\nCoeficientes obtidos usando Pandas DataFrame:")
        print(coeficientes_df)

    """