import numpy as np
import pandas as pd
df = pd.read_csv('vinho.csv')
print("conteudo da tabela, antes de normalizacao:")
df.head()

'''
Essa função realiza uma normalização de um valor `x` para uma escala entre 0 e 1, 
subtraindo o mínimo (`min`) e dividindo pelo range (`max - min`). 
Isso ajuda a padronizar valores em diferentes escalas para um intervalo comum.
'''
def MinMaxScale(x, min, max):
    valx_min =  (x - min)
    valx_max =  (max - min)
    val_result = valx_min / valx_max
    return (x - min) / (max - min)


mins = df.min()
maxs = df.max()

for column in df:
    df[column] = MinMaxScale(df[column], mins[column], maxs[column])

df.head()
print("Conteudo da tabela, após normalizacao:")

target = "is good"
features = df.columns.to_list()
features.remove(target)

from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

def distance(x, y):
    return np.sqrt(sum((x - y)**2))

class KNearestNeighbors:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X_val):
        # Lista para resultado
        y_pred = []
        # Para cada amostra de vale, vamos calcular sua distância até os dados de treino
        X_val_arr = X_val.to_numpy()
        X_train_arr = self.X_train.to_numpy()
        for row_val in X_val_arr:
            # Array para guardar [index_train, distancia]
            distances = []
            # Vamos percorrer os dados de treino colocando as distancias em nossa matriz
            for index_train, row_train in enumerate(X_train_arr):
                distances.append([index_train, distance(row_val, row_train)])
            # Vamos ordenar o array com base nas distancias (np.argsort retorna somente os indices)
            distances = sorted(distances, key=lambda x: x[1])
            # Pegando os k primeiros vizinhos
            nearestNeighbors = distances[0:self.k]
            # Ignorando agora as distancias
            nearestNeighbors = np.array(nearestNeighbors)[:,0]
            # Para cada vizinho, vamos analisar nos dados de treino o target
            result = []
            for neighbor in nearestNeighbors:
                result.append(y_train.to_numpy()[int(neighbor)])
            if np.array(result).sum() > len(result) / 2:
                y_pred.append(1)
            else:
                y_pred.append(0)

        return y_pred

    def accuracy(self, y_val, y_pred):
        total = 0
        for val, pred in zip(y_val, y_pred):
            if (val == pred):
                total += 1
        return total / len(y_val)

model = KNearestNeighbors(k=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_val)
model.accuracy(y_pred, y_val)

ks = [1, 3, 5, 7, 9]
for k in ks:
  model = KNearestNeighbors(k=k)
  model.fit(X_train, y_train)
  '''
  Essa linha de código calcula a precisão do modelo, ou seja, 
  a porcentagem de previsões corretas em relação ao total de previsões feitas. 
  Ela compara as previsões (`y_pred`) com os valores reais (`y_val`) 
  e retorna a precisão do modelo.
  '''
  y_pred = model.predict(X_val)
  print(model.accuracy(y_pred, y_val))

print("-------------------")

ks = [ 3,5]
for k in ks:
  model = KNearestNeighbors(k=k)
  model.fit(X_train, y_train)
  '''
  Essa linha de código calcula a precisão do modelo, ou seja, 
  a porcentagem de previsões corretas em relação ao total de previsões feitas. 
  Ela compara as previsões (`y_pred`) com os valores reais (`y_val`) 
  e retorna a precisão do modelo.
  '''
  y_pred = model.predict(X_val)
  print(model.accuracy(y_pred, y_val))
