import sympy as sp

x = sp.symbols('x')
expr = x**2 - 9
fatorado = sp.factor(expr)
print(fatorado)