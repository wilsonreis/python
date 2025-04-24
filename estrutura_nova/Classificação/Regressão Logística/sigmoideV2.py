import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 100)  # Criando 100 valores entre -10 e 10
print(x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
y = sigmoid(x)

# Exemplo de uso da função sigmoid
valor = np.linspace(1, 5, 5)
resultado = sigmoid(valor)
print(f"Sigmoid({valor}) = {resultado}")



# Gerando dados para o gráfico
x = np.linspace(-1, 1, 100)  # Criando 100 valores entre -10 e 10
y = sigmoid(x)

# Plotando o gráfico da função sigmoide
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.title('Função Sigmoide')
plt.grid(True)
plt.show()


