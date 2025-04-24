# Autores: Os desenvolvedores do scikit-learn
# SPDX-License-Identifier: BSD-3-Clause

# Importa o conjunto de dados iris
from sklearn.datasets import load_iris
iris = load_iris()  # Carrega o conjunto de dados iris

# Importa bibliotecas para plotagem e manipulação de arrays
import matplotlib.pyplot as plt
import numpy as np

# Importa bibliotecas para visualização de fronteiras de decisão e classificadores de árvore de decisão
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import DecisionTreeClassifier

# Define parâmetros para a plotagem
n_classes = 3  # Número de classes no conjunto de dados
plot_colors = "ryb"  # Cores para plotagem
plot_step = 0.02  # Passo para plotagem

# Loop para gerar plotagens para cada par de características
for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
    # Seleciona apenas as duas características correspondentes
    X = iris.data[:, pair]  # Seleciona as características
    y = iris.target  # Seleciona as classes

    # Treina um classificador de árvore de decisão
    clf = DecisionTreeClassifier().fit(X, y)  # Treina o classificador

    # Plota a fronteira de decisão
    ax = plt.subplot(2, 3, pairidx + 1)  # Cria um subplot
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)  # Ajusta o layout
    DecisionBoundaryDisplay.from_estimator(  # Plota a fronteira de decisão
        clf,  # Classificador
        X,  # Características
        cmap=plt.cm.RdYlBu,  # Mapeamento de cores
        response_method="predict",  # Método de resposta
        ax=ax,  # Subplot
        xlabel=iris.feature_names[pair[0]],  # Rótulo do eixo x
        ylabel=iris.feature_names[pair[1]],  # Rótulo do eixo y
    )

    # Plota os pontos de treinamento
    for i, color in zip(range(n_classes), plot_colors):  # Loop para cada classe
        idx = np.where(y == i)  # Seleciona os índices da classe
        plt.scatter(  # Plota os pontos
            X[idx, 0],  # Característica 1
            X[idx, 1],  # Característica 2
            c=color,  # Cor
            label=iris.target_names[i],  # Rótulo da classe
            edgecolor="black",  # Cor da borda
            s=15,  # Tamanho do ponto
        )

# Plota o título da figura
plt.suptitle("Decision surface of decision trees trained on pairs of features")

# Plota a legenda
plt.legend(loc="lower right", borderpad=0, handletextpad=0)

# Ajusta o tamanho da figura
_ = plt.axis("tight")

# Importa biblioteca para plotagem de árvores de decisão
from sklearn.tree import plot_tree

# Plota a árvore de decisão treinada com todas as características
plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)  # Treina o classificador
plot_tree(clf, filled=True)  # Plota a árvore
plt.title("Decision tree trained on all the iris features")  # Plota o título
plt.show()  # Mostra a figura