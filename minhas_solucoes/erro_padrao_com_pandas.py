import pandas as pd

# Definindo os valores
valores = [4, 8, 6, 5, 3]

# Criando uma série do Pandas
dados = pd.Series(valores)

# Calculando o desvio padrão
desvio_padrao = dados.std(ddof=1)  # ddof=1 para amostra

# Calculando o erro padrão
erro_padrao = desvio_padrao / (len(dados) ** 0.5)

print("O erro padrão é:", erro_padrao)