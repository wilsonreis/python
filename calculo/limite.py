import sympy as sp

x = sp.symbols('x')

f = (x - 1)/(sp.sqrt(x) - 1)

# Calcula o limite da função para x tendendo a 1
limite = sp.limit(f, x, 1)

print("Função:", f)
print("Limite de x tendendo a 1:", limite)