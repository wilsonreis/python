import sympy as sp

x = sp.symbols('x')

f_str = input("Digite a função: ")
f = sp.sympify(f_str)

var_str = input("Digite a variável tendendo a (ex: 1, inf, -inf): ")
var = sp.sympify(var_str)

# Calcula o limite da função para a variável tendendo a
limite = sp.limit(f, x, var)

print("Função:", f)
print("Variável tendendo a:", var)
print("Limite:", limite)
'''
lim x→0 1/x = oo
lim x→∞ x^2 = oo
lim x→-∞ x^2 = oo
sum(k**2, k=1, 10) representa o somatório de k**2 de k=1 a 10.
Σ(k**2, k=1, 10) representa o somatório de k**2 de k=1 a 10.
y = 2x + 3 --> 2 é o coeficiente angular e 3 o coeficiente linear
No contexto da equação linear y = 2x + 3, o termo 2 é o coeficiente angular, e sim, 
ele representa a taxa de variação da função em relação à variável independente x.

O coeficiente angular 2 indica que para cada unidade de x, a função y muda em 2 unidades. 
Isso significa que a taxa de variação da função é de 2 unidades de y para cada 1 unidade de x.

Portanto, sim, o coeficiente angular 2 e a taxa de variação são conceitos equivalentes nesse caso. 
O coeficiente angular 2 representa a taxa de variação da função em relação à variável independente x.

Então, você pode dizer que o coeficiente angular 2 é a taxa de variação da função em relação à variável independente x, 
e vice-versa.

3 mostra o deslocamento da reta em relação ao eixo y

coeficiente ou taxa de variação = tangente da reta (coeficiente angular) que
matemáticalmente --> tg de um angulo = cateto oposto / cateto adjacente 
C:\w\p\math_ml\tangente.jpg
'''