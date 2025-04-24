# prompt: crie um exemplo, baseado no scikit-learn, de regressão linear. Que seja simples mas mostre graficamente o gráfico de dispersão e a reta.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Gerar dados de exemplo
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 2 * X + 1 + np.random.randn(100, 1)

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Criar um modelo de regressão linear
model = LinearRegression()

# Treinar o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Fazer previsões com os dados de teste
y_pred = model.predict(X_test)

# Plotar os dados e a reta de regressão
plt.scatter(X_test, y_test, color='blue', label='Dados')
plt.plot(X_test, y_pred, color='red', label='Reta de Regressão')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regressão Linear')
plt.legend()
plt.show()
