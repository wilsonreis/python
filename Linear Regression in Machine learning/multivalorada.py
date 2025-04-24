import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Define os dados com múltiplas features (X) e múltiplos valores de saída (y)
# X terá 3 features (colunas) e 100 amostras (linhas)
# y terá 2 valores de saída (colunas) e 100 amostras (linhas)
num_samples = 100
num_features = 3
num_outputs = 2

# Gera dados aleatórios para X e y
X = np.random.rand(num_samples, num_features)
y = np.random.rand(num_samples, num_outputs)

# Cria o modelo de regressão linear multivariada
reg = LinearRegression()

# Treina o modelo com os dados
reg.fit(X, y)

# Faz previsões usando o modelo treinado
y_pred = reg.predict(X)

# Imprime os coeficientes da regressão (um conjunto para cada valor de saída)
print("Coeficientes de inclinação (β1):", reg.coef_)
print("Intercepto (β0):", reg.intercept_)


# Visualização (apenas para 2 features e 1 saída para simplificar a visualização)
# Se você tiver mais features, considere outras técnicas de visualização
if num_features == 2 and num_outputs == 1:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], y, color='blue')  # Pontos de dados reais
    ax.plot_trisurf(X[:, 0], X[:, 1], y_pred.flatten(), color='red', alpha=0.5) # Plano de regressão
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Saída')
    plt.title('Regressão Linear Multivariada')
    plt.show()
else:
    print("Visualização 3D não disponível para mais de 2 features ou mais de 1 saída.")