# prompt: Consegue refatorar o código abaixo, plotando o resultado no plano cartesiano:
# # prompt: consegue me fazer um script de Regressão Logística, bem simples? numa segunda fase pedirei para aumentar o grau de dificuldade.
# # Outro ponto, dentro do script coloque bastantes comentários explicativos
# # Importa as bibliotecas necessárias
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# # 1. Preparar os dados
# # Suponha que você tenha um conjunto de dados com recursos (X) e rótulos (y)
# # Exemplo de dados (substitua com seus próprios dados)
# X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
# y = np.array([0, 0, 1, 1, 1])  # Rótulos binários (0 ou 1)
# # 2. Dividir os dados em conjuntos de treinamento e teste
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# # 3. Criar e treinar o modelo de regressão logística
# model = LogisticRegression()
# model.fit(X_train, y_train)
# # 4. Fazer previsões no conjunto de teste
# y_pred = model.predict(X_test)
# # 5. Avaliar o modelo
# accuracy = accuracy_score(y_test, y_pred)
# print("Acurácia do modelo:", accuracy)
# # Exemplo de como fazer uma nova previsão com o modelo treinado
# # nova_amostra = np.array([[6, 7]])
# # previsao = model.predict(nova_amostra)
# # print("Previsão para a nova amostra:", previsao)

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Preparar os dados
# Suponha que você tenha um conjunto de dados com recursos (X) e rótulos (y)
# Exemplo de dados (substitua com seus próprios dados)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 1, 1, 1])  # Rótulos binários (0 ou 1)

# 2. Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Criar e treinar o modelo de regressão logística
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# 5. Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia do modelo:", accuracy)

# Plotar os dados e a fronteira de decisão
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Regressão Logística')

# Obter os coeficientes do modelo
coef = model.coef_[0]
intercept = model.intercept_[0]

# Criar a linha de separação (fronteira de decisão)
x_values = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100)
y_values = -(coef[0] * x_values + intercept) / coef[1]

plt.plot(x_values, y_values, 'r-')
plt.show()

# Exemplo de como fazer uma nova previsão com o modelo treinado
nova_amostra = np.array([[6, 7]])
previsao = model.predict(nova_amostra)
print("Previsão para a nova amostra:", previsao)
