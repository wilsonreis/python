
# Resultados dos Modelos de Classifica��o

## Dados Simulados

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import io
import base64

# Definindo uma semente para reprodutibilidade
np.random.seed(42)

# Gerando dados simulados
n_samples = 100
horas_estudo = np.random.uniform(1, 10, n_samples)  # Entre 1 e 10 horas
ultimas_notas = np.random.uniform(4, 10, n_samples)  # Notas entre 4 e 10

# Criando um label baseado em horas de estudo e notas (simula��o)
aprovado = (horas_estudo + ultimas_notas > 13).astype(int)

# Criando o DataFrame
data = {'horas_estudo': horas_estudo, 'ultimas_notas': ultimas_notas, 'aprovado': aprovado}
df = pd.DataFrame(data)

print(df.head())
```

## Regress�o Log�stica (Logistic Regression)

```python
# Separando features (X) e target (y)
X = df[['horas_estudo', 'ultimas_notas']]
y = df['aprovado']

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criando e treinando o modelo de Regress�o Log�stica
model = LogisticRegression()
model.fit(X_train, y_train)

# Fazendo previs�es
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acur�cia da Regress�o Log�stica: {accuracy}')
print("Fim Acur�cia da Regress�o Log�stica-----------------------------------------")
print("In�cio classification_report(y_test, y_pred)-----------------------------------------")
print(classification_report(y_test, y_pred))
print("Fim classification_report(y_test, y_pred)-----------------------------------------")
```

**Acur�cia da Regress�o Log�stica:** 0.43333333333333335

**Relat�rio de Classifica��o:**
```
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        17
           1       0.43      1.00      0.60        13

    accuracy                           0.43        30
   macro avg       0.22      0.50      0.30        30
weighted avg       0.19      0.43      0.26        30

```

## M�quinas de Vetores de Suporte (SVM)

```python
# Criando e treinando o modelo SVM
model = SVC(kernel='linear')  # Voc� pode experimentar diferentes kernels ('linear', 'rbf', 'poly', etc.)
model.fit(X_train, y_train)

# Fazendo previs�es
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acur�cia do SVM: {accuracy}')
print(classification_report(y_test, y_pred))
```

**Acur�cia do SVM:** 0.43333333333333335

**Relat�rio de Classifica��o:**
```
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        17
           1       0.43      1.00      0.60        13

    accuracy                           0.43        30
   macro avg       0.22      0.50      0.30        30
weighted avg       0.19      0.43      0.26        30

```

## �rvores de Decis�o (Decision Trees)

```python
# Criando e treinando o modelo de �rvore de Decis�o
model = DecisionTreeClassifier(max_depth=5)  # Voc� pode ajustar a profundidade m�xima
model.fit(X_train, y_train)

# Fazendo previs�es
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acur�cia da �rvore de Decis�o: {accuracy}')
print(classification_report(y_test, y_pred))
```

**Acur�cia da �rvore de Decis�o:** 0.43333333333333335

**Relat�rio de Classifica��o:**
```
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        17
           1       0.43      1.00      0.60        13

    accuracy                           0.43        30
   macro avg       0.22      0.50      0.30        30
weighted avg       0.19      0.43      0.26        30

```

## Florestas Aleat�rias (Random Forests)

```python
# Criando e treinando o modelo de Floresta Aleat�ria
model = RandomForestClassifier(n_estimators=100, random_state=42)  # n_estimators � o n�mero de �rvores
model.fit(X_train, y_train)

# Fazendo previs�es
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acur�cia da Floresta Aleat�ria: {accuracy}')
print(classification_report(y_test, y_pred))
```

**Acur�cia da Floresta Aleat�ria:** 0.43333333333333335

**Relat�rio de Classifica��o:**
```
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        17
           1       0.43      1.00      0.60        13

    accuracy                           0.43        30
   macro avg       0.22      0.50      0.30        30
weighted avg       0.19      0.43      0.26        30

```

## Redes Neurais Artificiais (Neural Networks)

```python
# Pr�-processamento: Escalonamento dos dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Criando e treinando o modelo de Rede Neural
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=10000, random_state=42)  # Ajuste as camadas e itera��es
model.fit(X_train_scaled, y_train)

# Fazendo previs�es
y_pred = model.predict(X_test_scaled)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acur�cia da Rede Neural: {accuracy}')
print(classification_report(y_test, y_pred))
```

**Acur�cia da Rede Neural:** 0.9666666666666667

**Relat�rio de Classifica��o:**
```
              precision    recall  f1-score   support

           0       1.00      0.94      0.97        17
           1       0.93      1.00      0.96        13

    accuracy                           0.97        30
   macro avg       0.96      0.97      0.97        30
weighted avg       0.97      0.97      0.97        30

```
