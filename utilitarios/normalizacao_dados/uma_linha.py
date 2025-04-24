import pandas as pd

# Carrega os dados
df = pd.read_csv('dados.csv')

# Define a função para escalar os dados
def scale_data(x):
    return (x - x.min()) / (x.max() - x.min())

# Aplica a escala Min-Max em cada coluna
df = df.apply(scale_data)

# Exibe o resultado
print(df)