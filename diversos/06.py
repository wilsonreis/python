import pandas as pd
from sklearn.model_selection import train_test_split

# Carregar o dataset de um arquivo CSV local
# Suponha que o arquivo se chame 'dados.csv' e que a última coluna seja o target
df = pd.read_csv('diabetes.csv')

# Separar as características do target
# Aqui estamos assumindo que a última coluna do CSV é o target
#X = df.iloc[:, :-1].values  # Todas as colunas, exceto a última
X = df.iloc[:, :3].values  # As 3 primeiras colunas
y = df.iloc[:, -1].values   # Última coluna

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Agora você pode prosseguir com o treinamento de um modelo, como no exemplo anterior
