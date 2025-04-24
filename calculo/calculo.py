import sympy as sp

# Defina a variável
x = sp.symbols('x')

# Defina a função
f = x**2

# Calcule a derivada da função
f_prime = sp.diff(f, x)

# Resolva a equação para encontrar o ponto mínimo
ponto_minimo = sp.solve(f_prime, x)

print(ponto_minimo)