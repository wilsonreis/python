import sympy as sp

# Defina a variável
x = sp.symbols('x')

# Defina a parábola
f = x**2 + 2*x + 1

# Calcule a taxa de variação (derivada)
f_prime = sp.diff(f, x)

# Calcule a taxa de variação em x = 2
taxa_variacao_em_x_2 = f_prime.subs(x, 2)

print(taxa_variacao_em_x_2)