from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar o dataset
iris = load_iris()
print(iris.keys())
print(iris.data)
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
#iris.data são as características (variáveis independentes).
#iris.target são os rótulos (variáveis dependentes).
#test_size=0.2: 20% dos dados serão usados para teste, 80% para treino.
#random_state=42: Garante que a divisão seja sempre a mesma ao executar o código.
print("iris.data[:5]    :",iris.data[:5])   # Exibe as primeiras 5 amostras (flores)
print("iris.target[:5]  :",iris.target[:5]) # Exibe os rótulos das primeiras 5 amostras


X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Criar e treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Fazer previsões
y_pred = knn.predict(X_test)

# Avaliar o modelo
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")


print(iris.feature_names)
print(iris.data)
print(iris.target)