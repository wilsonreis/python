import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

n_samples = 100
horas_estudo = np.random.uniform(1, 10, n_samples)
ultimas_notas = np.random.uniform(4, 10, n_samples)
aprovado = (horas_estudo + ultimas_notas > 13).astype(int)

data = {'horas_estudo': horas_estudo, 'ultimas_notas': ultimas_notas, 'aprovado': aprovado}
df = pd.DataFrame(data)

markdown_output = " "

markdown_output += df.head().to_markdown(index=False) + "\n```\n"

X = df[['horas_estudo', 'ultimas_notas']]
y = df['aprovado']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Regressão Logística
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

markdown_output += f"""
## 1. Regressão Logística (Logistic Regression)

Acurácia: {accuracy}

Relatório de Classificação:
```
{classification_report(y_test, y_pred)}
```
"""

# SVM
model = SVC(kernel='linear')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

markdown_output += f"""
## 2. Máquinas de Vetores de Suporte (SVM)

Acurácia: {accuracy}

Relatório de Classificação:
```
{classification_report(y_test, y_pred)}
```
"""

# Árvores de Decisão
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

markdown_output += f"""
## 3. Árvores de Decisão (Decision Trees)

Acurácia: {accuracy}

Relatório de Classificação:
```
{classification_report(y_test, y_pred)}
```
"""

# Florestas Aleatórias
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

markdown_output += f"""
## 4. Florestas Aleatórias (Random Forests)

Acurácia: {accuracy}

Relatório de Classificação:
```
{classification_report(y_test, y_pred)}
```
"""

# Redes Neurais Artificiais
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=10000, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

markdown_output += f"""
## 5. Redes Neurais Artificiais (Neural Networks)

Acurácia: {accuracy}

Relatório de Classificação:
```
{classification_report(y_test, y_pred)}
```
"""

with open("classification_results.md", "w") as file:
    file.write(markdown_output)
