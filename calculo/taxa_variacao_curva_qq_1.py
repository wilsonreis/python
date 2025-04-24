import sympy as sp

# Defina a variável
x = sp.symbols('x')

# Defina a curva
f = sp.sin(x) + 2*sp.cos(x)

# Calcule a taxa de variação (derivada)
f_prime = sp.diff(f, x)

# Calcule a taxa de variação em x = pi/4
taxa_variacao_em_x_pi_4 = f_prime.subs(x, sp.pi/4)

print(taxa_variacao_em_x_pi_4)