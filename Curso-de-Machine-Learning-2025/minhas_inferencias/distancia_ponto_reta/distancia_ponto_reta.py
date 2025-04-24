import math


def distancia_ponto_reta(x0, y0, a, b, c):
    """
    Calcula a distância entre um ponto (x0, y0) e uma reta definida por ax + by + c = 0.

    Parâmetros:
    - x0, y0: Coordenadas do ponto.
    - a, b, c: Coeficientes da equação da reta (ax + by + c = 0).

    Retorna:
    - A distância entre o ponto e a reta.
    """

    # Passo 1: Calcular o numerador |a*x0 + b*y0 + c|
    numerador = abs(a * x0 + b * y0 + c)

    # Passo 2: Calcular o denominador √(a² + b²)
    denominador = math.sqrt(a ** 2 + b ** 2)

    # Passo 3: Calcular a distância (numerador / denominador)
    distancia = numerador / denominador

    return distancia


# Exemplo de uso:
# Ponto P(2, 3)
x_ponto = 2
y_ponto = 3

# Reta r: 3x + 4y - 5 = 0 (a=3, b=4, c=-5)
a_reta = 3
b_reta = 4
c_reta = -5

# Chamando a função e armazenando o resultado
distancia = distancia_ponto_reta(x_ponto, y_ponto, a_reta, b_reta, c_reta)

# Exibindo o resultado
print(
    f"A distância entre o ponto ({x_ponto}, {y_ponto}) e a reta {a_reta}x + {b_reta}y + {c_reta} = 0 é: {distancia:.2f}")