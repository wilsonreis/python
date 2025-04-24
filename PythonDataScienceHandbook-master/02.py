import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

sns.set_style('whitegrid')

# Geração de dados aleatórios
rng = np.random.RandomState(1)
x = 10 * rng.rand(100, 1)  # Corrigido aqui
y = 0.5 + np.dot(x, [1.5])

# Plotagem dos dados
plt.scatter(x, y)
plt.show()

# Criação do modelo de regressão linear
model = LinearRegression(fit_intercept=True)

# Treinamento do modelo
model.fit(x, y)

# Geração de dados para plotagem da reta de ajuste
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

# Plotagem da reta de ajuste
plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()

# Impressão dos coeficientes do modelo
print("Model slope:    ", model.coef_[0])
print("Model intercept:", model.intercept_)