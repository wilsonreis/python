import sympy as sp

# Defina a variável
x = sp.symbols('x')

# Defina a curva
f = sp.sin(x) + 2*sp.cos(x)

# Calcule a taxa de variação (derivada)
f_prime = sp.diff(f, x)

print(f_prime)