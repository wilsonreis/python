# Making imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['figure.figsize'] = (12.0, 9.0)
plt.rcParams['figure.figsize'] = (5.0, 4.0)

'''
Essa linha de código é usada para definir o tamanho da figura (ou gráfico) que será criada com a biblioteca Matplotlib.
Aqui está uma explicação detalhada:
* `plt`: é o nome comummente usado para a biblioteca Matplotlib.
* `rcParams`: é um dicionário que contém as configurações padrão para a biblioteca Matplotlib.
* `figure.figsize`: é a chave do dicionário que define o tamanho da figura.
* `(12.0, 9.0)`: é o valor que define o tamanho da figura em polegadas.
Quando você define o tamanho da figura com essa linha de código, você está dizendo para a biblioteca Matplotlib criar figuras com um tamanho de 12 polegadas de largura e 9 polegadas de altura.
Isso é útil porque permite que você controle o tamanho da figura que será criada, o que pode ser importante para apresentações, relatórios ou publicações.
Aqui estão alguns exemplos de como você pode usar essa linha de código:
* `plt.rcParams['figure.figsize'] = (8.0, 6.0)`: cria uma figura com um tamanho de 8 polegadas de largura e 6 polegadas de altura.
* `plt.rcParams['figure.figsize'] = (10.0, 8.0)`: cria uma figura com um tamanho de 10 polegadas de largura e 8 polegadas de altura.
* `plt.rcParams['figure.figsize'] = (15.0, 12.0)`: cria uma figura com um tamanho de 15 polegadas de largura e 12 polegadas de altura.
Lembre-se de que o tamanho da figura também pode ser definido em outras unidades, como pixels ou centímetros, usando as seguintes chaves:
* `figure.dpi`: define a resolução da figura em pixels por polegada.
* `figure.figwidth`: define a largura da figura em polegadas.
* `figure.figheight`: define a altura da figura em polegadas.
Por exemplo, você pode definir o tamanho da figura em pixels usando a seguinte linha de código:
```python
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (800, 600)
```
Isso criaria uma figura com um tamanho de 800 pixels de largura e 600 pixels de altura, com uma resolução de 100 pixels por polegada.
'''

# Preprocessing Input data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)
plt.show()

# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean

print (m, c)

# Making predictions
Y_pred = m*X + c

plt.scatter(X, Y) # actual
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()