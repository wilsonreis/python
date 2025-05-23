# prompt: construa um script , com bastante comentário, explicando a função  sigmoide

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  """
  Função Sigmoide.

  Esta função calcula a função sigmoide para um dado valor de entrada x.
  A função sigmoide é uma função matemática que mapeia qualquer valor real
  para um valor entre 0 e 1. Ela é amplamente utilizada em aprendizado de máquina,
  especialmente em redes neurais, como uma função de ativação.

  Args:
    x: Um valor real ou um array de valores reais.

  Returns:
    O valor da função sigmoide para x.
  """
  return 1 / (1 + np.exp(-x))

# Gerando dados para o gráfico
x = np.linspace(-10, 10, 100)  # Criando 100 valores entre -10 e 10
y = sigmoid(x)

# Plotando o gráfico da função sigmoide
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.title('Função Sigmoide')
plt.grid(True)
plt.show()

# Exemplo de uso da função sigmoid
valor = [2,3]
resultado = sigmoid(valor)
print(f"Sigmoid({valor}) = {resultado}")


# Explicação detalhada da função sigmoide:
"""
A função sigmoide é definida como:

Sigmoid(x) = 1 / (1 + e^(-x))

Onde:
- x é a entrada da função.
- e é a constante matemática "e" (aproximadamente 2.71828).

A função sigmoide tem as seguintes características:

- Seu valor de saída sempre está entre 0 e 1. 
- Quando x é um número muito grande e positivo, a função se aproxima de 1.
- Quando x é um número muito grande e negativo, a função se aproxima de 0.
- Quando x é igual a 0, a função retorna 0.5.

A função sigmoide é útil em problemas de classificação binária, pois pode ser
interpretada como a probabilidade de um determinado exemplo pertencer a uma
determinada classe. Por exemplo, se a função sigmoid retornar 0.8 para um
determinado exemplo, isso indica que existe uma probabilidade de 80% de que
esse exemplo pertença à classe positiva.


"""