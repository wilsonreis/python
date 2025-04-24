import numpy as np
import matplotlib.pyplot as plt

# Pontos dados
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11, 13])

# Cálculo da média de x e y
x_media = np.mean(x)
y_media = np.mean(y)

# Cálculo da inclinação (m) e do intercepto (b)
m = np.sum((x - x_media) * (y - y_media)) / np.sum((x - x_media) ** 2)
b = y_media - m * x_media

print("Grau de inclinação (m):", m)

# Modelo linear
def modelo_linear(x):
    return m * x + b

# Previsão do valor de y para x = 2,5
x_previsto = 2.5
y_previsto = modelo_linear(x_previsto)

print("Previsão do valor de y para x = 2,5:", y_previsto)

# Criando um array de x para plotar o modelo linear
x_plot = np.linspace(2, 5, 100)

# Plotando os pontos e o modelo linear
plt.scatter(x, y, label='Pontos dados')
plt.plot(x_plot, modelo_linear(x_plot), label='Modelo linear', color='red')
plt.scatter(x_previsto, y_previsto, label='Previsão', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Modelo Linear')
plt.legend()
plt.show()