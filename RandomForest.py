import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.inspection import permutation_importance

# 1. Carregamento e Preparação dos Dados

# Explicação:
# Vamos usar um dataset popular para classificação, o Iris dataset, que já vem embutido no scikit-learn.
# Ele contém medidas de sépalas e pétalas de três espécies de íris (Setosa, Versicolor e Virginica).
# Este dataset é adequado para demonstrar o RandomForest porque é um problema de classificação multiclasse relativamente simples,
# permitindo focar na aplicação do modelo e na interpretação dos resultados.

from sklearn.datasets import load_iris
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target
data['target_names'] = [iris.target_names[i] for i in iris.target] # Adiciona o nome das especies

# Visualizando os dados (opcional, mas útil para entender o dataset)
print("Amostra dos dados:")
print(data.head())

# 2. Divisão dos Dados em Treino e Teste

# Explicação:
# É crucial dividir os dados em um conjunto de treino para o modelo aprender e um conjunto de teste para avaliar seu desempenho
# em dados não vistos.  A divisão típica é 80/20 (treino/teste), mas isso pode variar dependendo do tamanho do dataset.
# O random_state garante que a divisão seja a mesma a cada execução, facilitando a reprodução dos resultados.

X = data[iris.feature_names]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Inicialização e Treinamento do Modelo Random Forest

# Explicação:
# RandomForest é um algoritmo de ensemble learning que constrói múltiplas árvores de decisão e as combina para obter uma
# predição mais precisa e robusta.

# Por que Random Forest?
# * Alta precisão: Geralmente produz resultados muito bons sem muita necessidade de ajuste fino.
# * Robustez:  Menos propenso a overfitting do que uma única árvore de decisão.
# * Importância das Features:  Fornece uma estimativa da importância de cada feature para a predição, auxiliando na interpretação.
# * Versatilidade:  Funciona bem com dados numéricos e categóricos.
# * Lida bem com dados faltantes.

# Ajustando os hiperparâmetros:
# n_estimators: Número de árvores na floresta.  Mais árvores geralmente levam a melhor desempenho, mas com custo computacional maior.
# random_state: Garante a reprodutibilidade do modelo.

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 4. Predição e Avaliação do Modelo

# Explicação:
# Após treinar o modelo, o utilizamos para fazer predições no conjunto de teste.
# A acurácia e o relatório de classificação fornecem uma avaliação abrangente do desempenho do modelo.

y_pred = rf_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2f}")

print("Relatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 5. Importância das Features

# Explicação:
# Uma das vantagens do Random Forest é a capacidade de estimar a importância de cada feature.
# Isso pode ajudar a entender quais features são mais relevantes para a predição e potencialmente simplificar o modelo.

feature_importances = rf_model.feature_importances_

# Plotando a importância das features
plt.figure(figsize=(10, 6))
plt.bar(X.columns, feature_importances)
plt.xlabel("Features")
plt.ylabel("Importância")
plt.title("Importância das Features no Modelo Random Forest")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 6. (Opcional) Análise de Permutação da Importância das Features

# Explicação:
# A importância de permutação é outra forma de avaliar a importância das features.  Ela calcula a diminuição na acurácia
# do modelo quando uma feature é aleatoriamente embaralhada.  Features mais importantes causarão uma maior diminuição na acurácia.
# É um método mais robusto do que a importância das features padrão, pois leva em consideração a interação entre as features.

result = permutation_importance(rf_model, X_test, y_test, n_repeats=10, random_state=42)
importance = result.importances_mean

# Plotando a importância da permutação
plt.figure(figsize=(10, 6))
plt.bar(X.columns, importance)
plt.xlabel("Features")
plt.ylabel("Importância (Permutação)")
plt.title("Importância das Features (Permutação) no Modelo Random Forest")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 7. (Opcional) Matriz de Confusão

# Explicação:
# A matriz de confusão fornece uma visão detalhada de como o modelo está classificando cada classe.
# Ela mostra o número de instâncias que foram corretamente classificadas e o número de instâncias que foram
# classificadas incorretamente em cada classe.

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Matriz de Confusão")
plt.show()