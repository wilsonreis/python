import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Define os dados com inclinação 2
X = np.array([0, 1, 2]).reshape(-1, 1)  # X precisa ser uma matriz 2D
y = 2 * X[:, 0]  # y = 2x (inclinação 2, intercepto 0)

# Cria o modelo de regressão linear
reg = linear_model.LinearRegression()

# Ajusta o modelo aos dados
reg.fit(X, y)

# Imprime os coeficientes
print("Coeficiente de inclinação (β1):", reg.coef_[0])
print("Intercepto (β0):", reg.intercept_)

# Plota os dados e a reta de regressão
plt.scatter(X, y)
plt.plot(X, reg.predict(X), color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear - Inclinação 2')
plt.show()