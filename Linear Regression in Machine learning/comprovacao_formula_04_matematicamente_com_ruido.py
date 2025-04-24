import numpy as np
import matplotlib.pyplot as plt

# Define os dados com ruído
X = np.array([0, 1, 2])
ruido = np.random.normal(0, 0.5, 3)  # Ruído com desvio padrão 0.5
y = 2 * X + ruido  # y = 2x + ruido

# Calcula a inclinação (β1) e o intercepto (β0)
x_mean = np.mean(X)
y_mean = np.mean(y)

beta1 = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean)**2)
beta0 = y_mean - beta1 * x_mean

# Imprime os coeficientes
print("Coeficiente de inclinação (β1):", beta1)
print("Intercepto (β0):", beta0)

# Calcula os valores de y previstos
y_pred = beta1 * X + beta0

# Calcula o erro (resíduos)
erro = y - y_pred

# Imprime o erro
print("Erro (resíduos):", erro)

# Plota os dados, a reta de regressão e os erros
plt.scatter(X, y)
plt.plot(X, y_pred, color='red', label='Regressão')
# Take the absolute value of the error to ensure it's non-negative
plt.errorbar(X, y_pred, yerr=np.abs(erro), fmt='o', color='red', label='Erros') # adiciona as barras de erro
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear com Ruído e Erro')
plt.legend() # adiciona legenda
plt.show()

'''
Modelo de Regressão:

O script usa um modelo de Regressão Linear Simples. Isso significa que ele tenta encontrar a melhor linha reta que representa a relação entre uma variável independente (X) e uma variável dependente (y). A equação da linha é da forma:

 
y = β0 + β1 * x
Use code with caution
Onde:

y é a variável dependente (o que você está tentando prever).
x é a variável independente (o preditor).
β0 é o intercepto (o valor de y quando x é 0).
β1 é a inclinação (o quanto y muda para cada mudança de unidade em x).
No script, a regressão linear é calculada manualmente usando as fórmulas para β0 e β1, e também é visualizada usando a biblioteca matplotlib.

Modelo de Erro:

O script considera o Erro Absoluto para representar a diferença entre os valores reais (y) e os valores previstos (y_pred). O erro é calculado como:

 
erro = y - y_pred
Use code with caution
No entanto, como matplotlib exige que as barras de erro (yerr) sejam não negativas, o script usa o valor absoluto do erro (np.abs(erro)) para garantir que as barras de erro sejam exibidas corretamente.

Em resumo:

Modelo de Regressão: Regressão Linear Simples
Modelo de Erro: Erro Absoluto (e sua representação visual com barras de erro usando o valor absoluto)
'''