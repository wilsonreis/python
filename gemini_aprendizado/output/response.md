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

def generate_markdown(df):
    """
    Gera o conteúdo do arquivo Markdown com os resultados dos modelos de classificação.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados simulados.

    Returns:
        str: Conteúdo do arquivo Markdown.
    """

    markdown_content = f"""
# Resultados dos Modelos de Classificação

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

# Criando um label baseado em horas de estudo e notas (simulação)
aprovado = (horas_estudo + ultimas_notas > 13).astype(int)

# Criando o DataFrame
data = {{'horas_estudo': horas_estudo, 'ultimas_notas': ultimas_notas, 'aprovado': aprovado}}
df = pd.DataFrame(data)

print(df.head())
```

## Regressão Logística (Logistic Regression)

```python
# Separando features (X) e target (y)
X = df[['horas_estudo', 'ultimas_notas']]
y = df['aprovado']

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criando e treinando o modelo de Regressão Logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Regressão Logística: {{accuracy}}')
print("Fim Acurácia da Regressão Logística-----------------------------------------")
print("Início classification_report(y_test, y_pred)-----------------------------------------")
print(classification_report(y_test, y_pred))
print("Fim classification_report(y_test, y_pred)-----------------------------------------")
```

**Acurácia da Regressão Logística:** {accuracy_score(y_test, model.predict(X_test))}

**Relatório de Classificação:**
```
{classification_report(y_test, model.predict(X_test))}
```

## Máquinas de Vetores de Suporte (SVM)

```python
# Criando e treinando o modelo SVM
model = SVC(kernel='linear')  # Você pode experimentar diferentes kernels ('linear', 'rbf', 'poly', etc.)
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do SVM: {{accuracy}}')
print(classification_report(y_test, y_pred))
```

**Acurácia do SVM:** {accuracy_score(y_test, model.predict(X_test))}

**Relatório de Classificação:**
```
{classification_report(y_test, model.predict(X_test))}
```

## Árvores de Decisão (Decision Trees)

```python
# Criando e treinando o modelo de Árvore de Decisão
model = DecisionTreeClassifier(max_depth=5)  # Você pode ajustar a profundidade máxima
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Árvore de Decisão: {{accuracy}}')
print(classification_report(y_test, y_pred))
```

**Acurácia da Árvore de Decisão:** {accuracy_score(y_test, model.predict(X_test))}

**Relatório de Classificação:**
```
{classification_report(y_test, model.predict(X_test))}
```

## Florestas Aleatórias (Random Forests)

```python
# Criando e treinando o modelo de Floresta Aleatória
model = RandomForestClassifier(n_estimators=100, random_state=42)  # n_estimators é o número de árvores
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Floresta Aleatória: {{accuracy}}')
print(classification_report(y_test, y_pred))
```

**Acurácia da Floresta Aleatória:** {accuracy_score(y_test, model.predict(X_test))}

**Relatório de Classificação:**
```
{classification_report(y_test, model.predict(X_test))}
```

## Redes Neurais Artificiais (Neural Networks)

```python
# Pré-processamento: Escalonamento dos dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Criando e treinando o modelo de Rede Neural
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=10000, random_state=42)  # Ajuste as camadas e iterações
model.fit(X_train_scaled, y_train)

# Fazendo previsões
y_pred = model.predict(X_test_scaled)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Rede Neural: {{accuracy}}')
print(classification_report(y_test, y_pred))
```

**Acurácia da Rede Neural:** {accuracy_score(y_test, model.predict(X_test_scaled))}

**Relatório de Classificação:**
```
{classification_report(y_test, model.predict(X_test_scaled))}
```
"""
    
    return markdown_content

# Definindo uma semente para reprodutibilidade
np.random.seed(42)

# Gerando dados simulados
n_samples = 100
horas_estudo = np.random.uniform(1, 10, n_samples)  # Entre 1 e 10 horas
ultimas_notas = np.random.uniform(4, 10, n_samples)  # Notas entre 4 e 10

# Criando um label baseado em horas de estudo e notas (simulação)
aprovado = (horas_estudo + ultimas_notas > 13).astype(int)

# Criando o DataFrame
data = {'horas_estudo': horas_estudo, 'ultimas_notas': ultimas_notas, 'aprovado': aprovado}
df = pd.DataFrame(data)

print(df.head())

# 1. Regressão Logística (Logistic Regression)
# Separando features (X) e target (y)
X = df[['horas_estudo', 'ultimas_notas']]
y = df['aprovado']

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criando e treinando o modelo de Regressão Logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Regressão Logística: {accuracy}')
print("Fim Acurácia da Regressão Logística-----------------------------------------")
print("Início classification_report(y_test, y_pred)-----------------------------------------")
print(classification_report(y_test, y_pred))
print("Fim classification_report(y_test, y_pred)-----------------------------------------")

# 2. Máquinas de Vetores de Suporte (SVM) (Support Vector Machines)

# Criando e treinando o modelo SVM
model = SVC(kernel='linear')  # Você pode experimentar diferentes kernels ('linear', 'rbf', 'poly', etc.)
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do SVM: {accuracy}')
print(classification_report(y_test, y_pred))

# 3. Árvores de Decisão (Decision Trees)

# Criando e treinando o modelo de Árvore de Decisão
model = DecisionTreeClassifier(max_depth=5)  # Você pode ajustar a profundidade máxima
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Árvore de Decisão: {accuracy}')
print(classification_report(y_test, y_pred))

# 4. Florestas Aleatórias (Random Forests)

# Criando e treinando o modelo de Floresta Aleatória
model = RandomForestClassifier(n_estimators=100, random_state=42)  # n_estimators é o número de árvores
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Floresta Aleatória: {accuracy}')
print(classification_report(y_test, y_pred))

# 5. Redes Neurais Artificiais (Neural Networks)

# Pré-processamento: Escalonamento dos dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Criando e treinando o modelo de Rede Neural
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=10000, random_state=42)  # Ajuste as camadas e iterações
model.fit(X_train_scaled, y_train)

# Fazendo previsões
y_pred = model.predict(X_test_scaled)

# Avaliando o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia da Rede Neural: {accuracy}')
print(classification_report(y_test, y_pred))

# Gerar e salvar o arquivo Markdown
markdown_output = generate_markdown(df)
with open("resultados_classificacao.md", "w") as file:
    file.write(markdown_output)
```