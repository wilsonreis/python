# Importe as bibliotecas necessárias
import sys
import matplotlib
matplotlib.use('Agg')  # Use o backend Agg para gerar imagens em formato PNG

import matplotlib.pyplot as plt  # Importe o módulo pyplot do Matplotlib
from sklearn.neighbors import KNeighborsClassifier  # Importe o classificador K-Nearest Neighbors do Scikit-learn

# Defina os dados
x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]  # Coordenadas x dos pontos
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]  # Coordenadas y dos pontos
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]  # Classes dos pontos

# Imprima uma amostra dos dados
print("Amostra dos dados:")
print("x:", x[:5])  # Imprima as primeiras 5 coordenadas x
print("y:", y[:5])  # Imprima as primeiras 5 coordenadas y
print("classes:", classes[:5])  # Imprima as primeiras 5 classes

# Crie um conjunto de dados com as coordenadas x e y
data = list(zip(x, y))  # Crie um conjunto de dados com as coordenadas x e y

# Crie um classificador K-Nearest Neighbors com 1 vizinho
knn = KNeighborsClassifier(n_neighbors=1)  # Crie um classificador K-Nearest Neighbors com 1 vizinho

# Treine o classificador com os dados
knn.fit(data, classes)  # Treine o classificador com os dados

# Defina um novo ponto para classificar
new_x = 8  # Coordenada x do novo ponto
new_y = 21  # Coordenada y do novo ponto
new_point = [(new_x, new_y)]  # Crie um conjunto de dados com o novo ponto

# Classifique o novo ponto
prediction = knn.predict(new_point)  # Classifique o novo ponto

# Crie um gráfico com os dados e o novo ponto
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])  # Crie um gráfico com os dados e o novo ponto
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")  # Adicione um texto ao gráfico com a classe do novo ponto

# Salve a imagem em um arquivo PNG
plt.savefig('imagem.png')  # Salve a imagem em um arquivo PNG