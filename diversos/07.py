import numpy as np
import matplotlib.pyplot as plt

# Pontos dados
x = np.array([3.5, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37])
y = np.array([18, 15, 18, 16, 15, 14, 24])

# Cálculo da média de x e y
x_media = np.mean(x)
y_media = np.mean(y)

# Cálculo da inclinação (m) e do intercepto (b)
m = np.sum((x - x_media) * (y - y_media)) / np.sum((x - x_media) ** 2)
b = y_media - m * x_media

# Modelo linear
def modelo_linear(x):
    return m * x + b

# Criando um array de x para plotar o modelo linear
x_plot = np.linspace(2, 5, 100)

print("Grau de inclinação (m):", m)
print("Intercepto (b):", b)

# Plotando os pontos e o modelo linear
plt.scatter(x, y, label='Pontos dados')
plt.plot(x_plot, modelo_linear(x_plot), label='Modelo linear', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Modelo Linear')
plt.legend()
plt.show()