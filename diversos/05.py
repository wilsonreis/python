import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Carregar o conjunto de dados Diabetes
diabetes = datasets.load_diabetes()

# Selecionar as três primeiras características para simplificar
X = diabetes.data[:, :3]  # Aqui estamos pegando as três primeiras características
y = diabetes.target

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de regressão linear
model = LinearRegression()

# Treinar o modelo usando as características selecionadas
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
print('Coefficients: \n', model.coef_)
print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
print('Coefficient of determination R^2: %.2f' % r2_score(y_test, y_pred))

# Como estamos usando 3 características, não podemos mais plotar em um gráfico 2D simples.
# No entanto, podemos plotar a relação entre cada característica e o target previsto vs real.
for i in range(3):
    plt.figure(i)
    plt.scatter(X_test[:, i], y_test, color='black', label='Real')
    plt.scatter(X_test[:, i], y_pred, color='blue', label='Previsto')
    plt.xlabel('Característica {}'.format(i+1))
    plt.ylabel('Valor target')
    plt.legend()
    plt.show()

