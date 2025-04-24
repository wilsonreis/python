import sympy as sp

x = sp.symbols('x')

f_str = input("Digite a função: ")
f = sp.sympify(f_str)

# Calcula o limite da função para x tendendo a 1
limite = sp.limit(f, x, 1)

print("Função:", f)
print("Valor da função para x tendendo a 1:", limite)
# função (x - 1)/(sqrt(x) - 1)


#inf = float('inf')
#modulo = abs(x)
