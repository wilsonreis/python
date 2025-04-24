import numpy as np
import matplotlib.pyplot as plt

def funcao_sigmoide(z: np.ndarray) -> np.ndarray:
    """
    Calcula a função sigmoide para cada elemento em um array NumPy.

    A função sigmoide é definida como:
    sigma(z) = 1 / (1 + exp(-z))

    Args:
        z (np.ndarray): Um array NumPy de valores.

    Returns:
        np.ndarray: Um array NumPy com os valores da função sigmoide
                    calculados para cada elemento de 'z'.
    """
    return 1 / (1 + np.exp(-z))


# Cria um array de valores para o eixo x (z)
z = np.linspace(-10, 10, 400)  # Gera 400 pontos entre -10 e 10
#Um número maior de pontos resulta em uma curva mais suave.

# Calcula os valores correspondentes da função sigmoide
sigma_z = funcao_sigmoide(z)

# Cria o gráfico
plt.figure(figsize=(8, 6))  # Ajusta o tamanho da figura
plt.plot(z, sigma_z, label='σ(z) = 1 / (1 + exp(-z))')

# Adiciona título e rótulos aos eixos
plt.title('Função Sigmoide')
plt.xlabel('z')
plt.ylabel('σ(z)')

# Adiciona uma grade para facilitar a visualização
plt.grid(True)

# Adiciona a legenda
plt.legend()

# Adiciona linhas horizontais em y=0 e y=1
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.axhline(1, color='black', linestyle='--', linewidth=0.5)

# Adiciona linha vertical em x=0
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)

# Mostra o gráfico
plt.show()