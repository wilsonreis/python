# Queremos prever a eficiência de combustível de um carro em milhas por galão com base no peso do carro e temos o seguinte conjunto de dados:

Libras em 1.000 (recurso) Milhas por galão (rótulo) 3.5 18 3,69 15 3,44 18 3,43 16 4,34 15 4,42 14 2,37 24

utilize a regressão linear com diagrama de dispersão

Claro, aqui estão os passos sobre como usar a regressão linear com um diagrama de dispersão para prever a eficiência de combustível de um carro em milhas por galão com base no peso do carro, juntamente com um exemplo usando o conjunto de dados fornecido:

Passo 1: Importar as bibliotecas necessárias

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
Use o código com cuidado
Passo 2: Criar um DataFrame pandas com os dados fornecidos

data = {'Libras em 1.000': [3.5, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37],
        'Milhas por galão': [18, 15, 18, 16, 15, 14, 24]}
df = pd.DataFrame(data)
Use o código com cuidado
Passo 3: Criar um diagrama de dispersão dos dados

plt.scatter(df['Libras em 1.000'], df['Milhas por galão'])
plt.xlabel('Libras em 1.000')
plt.ylabel('Milhas por galão')
plt.title('Diagrama de dispersão de libras vs. milhas por galão')
plt.show()
Use o código com cuidado
Passo 4: Dividir os dados em conjuntos de treinamento e teste

X = df[['Libras em 1.000']]
y = df['Milhas por galão']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Dividir os dados com um tamanho de teste de 20%
Use o código com cuidado
Passo 5: Criar e treinar um modelo de regressão linear

model = LinearRegression()
model.fit(X_train, y_train)
Use o código com cuidado
Passo 6: Fazer previsões sobre os dados de teste

y_pred = model.predict(X_test)
Use o código com cuidado
Passo 7: Avaliar o modelo

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Erro quadrático médio:', mse)
print('R-quadrado:', r2)
Use o código com cuidado
Passo 8: Plotar a linha de regressão no diagrama de dispersão

plt.scatter(df['Libras em 1.000'], df['Milhas por galão'])
plt.plot(X_test, y_pred, color='red')
plt.xlabel('Libras em 1.000')
plt.ylabel('Milhas por galão')
plt.title('Regressão Linear de libras vs. milhas por galão')
plt.show()
Use o código com cuidado
Isso mostrará um diagrama de dispersão dos dados com a linha de regressão plotada nele. A linha de regressão representa a relação entre o peso do carro e a eficiência de combustível. Você pode usar esta linha para prever a eficiência de combustível de um carro com base em seu peso.

Por exemplo, se um carro pesa 3.000 libras, você pode prever sua eficiência de combustível encontrando o ponto na linha de regressão que corresponde a 3.000 libras no eixo x. A eficiência de combustível correspondente no eixo y seria a eficiência de combustível prevista para o carro.

Observação:

O conjunto de dados fornecido é muito pequeno, portanto, o modelo de regressão linear pode não ser muito preciso. Com mais dados, o modelo seria mais preciso.