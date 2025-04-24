import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler

# Definição dos nomes das colunas
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

# Carregamento do dataset
try:
    pima = pd.read_csv("diabetes.csv", header=0, names=col_names)  # Corrected: header=0 to use col_names
except FileNotFoundError:
    print("Erro: Arquivo diabetes.csv não encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    exit()

# Exibição das primeiras linhas do dataset
print(pima.head())

# Separação das variáveis de características e da variável alvo
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols]  # Features
y = pima['label']       # Target variable

# Divisão dos dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Escalonamento das características usando StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definição da grade de parâmetros para otimização
param_grid = {
    'penalty': ['l1', 'l2'],  # Regularização L1 (Lasso) e L2 (Ridge)
    'C': np.logspace(-4, 4, 20),  # Inverso da força da regularização
    'solver': ['liblinear']  # Solver adequado para L1 e L2 com pequenos datasets
}

# Otimização do modelo com GridSearchCV e validação cruzada
grid_search = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Exibição dos melhores parâmetros encontrados
print("Melhores parâmetros encontrados:", grid_search.best_params_)

# Criação do modelo de Regressão Logística com os melhores parâmetros
logreg = grid_search.best_estimator_

# Treinamento do modelo com os dados de treinamento
logreg.fit(X_train, y_train)

# Predição nos dados de teste
y_pred = logreg.predict(X_test)

# Avaliação do modelo
cnf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:\n", cnf_matrix)

# Visualização da matriz de confusão
class_names = ['Não Diabético', 'Diabético']
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names, rotation=45)
plt.yticks(tick_marks, class_names)

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g', xticklabels=class_names, yticklabels=class_names)
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Matriz de Confusão', y=1.1)
plt.ylabel('Rótulo Atual')
plt.xlabel('Rótulo Predito')
plt.show()

# Métricas de avaliação
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Precisão:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))

# Curva ROC e AUC
y_pred_proba = logreg.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)

plt.plot(fpr, tpr, label="AUC = "+str(auc))
plt.legend(loc=4)
plt.title('Curva ROC')
plt.xlabel('Taxa de Falso Positivo')
plt.ylabel('Taxa de Verdadeiro Positivo')
plt.show()