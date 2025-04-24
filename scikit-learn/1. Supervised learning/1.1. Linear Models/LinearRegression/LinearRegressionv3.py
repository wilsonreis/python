import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Pontos dados
x = np.array([3.5, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37]).reshape(-1, 1)
y = np.array([18, 15, 18, 16, 15, 14, 24])

# Criação do modelo de regressão linear
modelo = LinearRegression()

# Treinamento do modelo
modelo.fit(x, y)

# Previsão do valor de y para x = 2,5
x_previsto = np.array([[2.5]])
y_previsto = modelo.predict(x_previsto)

print("Valor de y para x = 2,5:", y_previsto)
print("Grau de inclinação (m): ",modelo.coef_)
print("Intercept_ :", modelo.intercept_)

# Criando um array de x para plotar o modelo linear
x_plot = np.linspace(2, 5, 100).reshape(-1, 1)

# Criando o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Pontos de dados')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Dispersão')
plt.legend()
plt.grid(True)
plt.show()

# Plotando os gráficos
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.scatter(x, y, label='Pontos dados')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de Dispersão')
plt.legend()
plt.xlim(2, 5)
plt.ylim(0, 24)

plt.subplot(1, 3, 2)
plt.plot(x_plot, modelo.predict(x_plot), label='Modelo linear', color='red')
plt.scatter(x, y, label='Pontos dados')
plt.scatter(x_previsto, y_previsto, label='Previsão', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Modelo Linear')
plt.legend()
plt.xlim(2, 5)
plt.ylim(0, 24)

plt.subplot(1, 3, 3)
plt.plot(x_plot, modelo.predict(x_plot), label='Modelo linear', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Reta')
plt.legend()
plt.xlim(2, 5)
plt.ylim(0, 24)

plt.tight_layout()
plt.show()