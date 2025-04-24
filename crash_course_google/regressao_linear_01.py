# Passo 1: Importar as bibliotecas necessárias

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Passo 2: Criar um DataFrame pandas com os dados fornecidos
data = {'Libras em 1.000': [3.5, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37],
        'Milhas por galão': [18, 15, 18, 16, 15, 14, 24]}
df = pd.DataFrame(data)

# Passo 3: Criar um diagrama de dispersão dos dados
plt.scatter(df['Libras em 1.000'], df['Milhas por galão'])
plt.xlabel('Libras em 1.000')
plt.ylabel('Milhas por galão')
plt.title('Diagrama de dispersão de libras vs. milhas por galão')
plt.show()

# Passo 4: Dividir os dados em conjuntos de treinamento e teste
X = df[['Libras em 1.000']]
y = df['Milhas por galão']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Dividir os dados com um tamanho de teste de 20%

# Passo 5: Criar e treinar um modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Passo 6: Fazer previsões sobre os dados de teste
y_pred = model.predict(X_test)

# Passo 7: Avaliar o modelo
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Erro quadrático médio:', mse)
print('R-quadrado:', r2)

# Passo 8: Plotar a linha de regressão no diagrama de dispersão
plt.scatter(df['Libras em 1.000'], df['Milhas por galão'])
plt.plot(X_test, y_pred, color='red')
plt.xlabel('Libras em 1.000')
plt.ylabel('Milhas por galão')
plt.title('Regressão Linear de libras vs. milhas por galão')
plt.show()

