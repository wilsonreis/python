import pandas as pd

# Criar uma série com os dados
dados = pd.Series([4, 8, 6, 5, 3])

# Calcular o desvio padrão
desvio_padrao = dados.std(ddof=1)  # ddof=1 para desvio padrão da amostra

print("O desvio padrão é:", desvio_padrao)