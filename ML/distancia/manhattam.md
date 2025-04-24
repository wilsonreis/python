### 📌 **Distância de Manhattan: Entendimento Matemático e Aplicação no KNN em Python**  

A **distância de Manhattan** é uma das formas de medir a distância entre dois pontos em um espaço multidimensional. Ela é conhecida também como **distância do táxi** ou **distância L1**, porque reflete o caminho percorrido em uma grade, como as ruas de Manhattan.  

---

## 🔹 **Definição Matemática da Distância de Manhattan**  
Dada duas coordenadas \( P = (x_1, y_1) \) e \( Q = (x_2, y_2) \), a distância de Manhattan é definida como:

\[
D_{Manhattan}(P, Q) = |x_2 - x_1| + |y_2 - y_1|
\]

Em um espaço multidimensional, a fórmula se generaliza para \( n \) dimensões:

\[
D_{Manhattan}(P, Q) = \sum_{i=1}^{n} |x_i - y_i|
\]

---

## 🔹 **Exemplo Manual**  

Se tivermos os pontos \( P(2, 3) \) e \( Q(5, 7) \), então:

\[
D_{Manhattan}(P, Q) = |5 - 2| + |7 - 3| = 3 + 4 = 7
\]

---

## 🔹 **Implementação em Python**  

Podemos calcular a distância de Manhattan usando **NumPy** e **scipy.spatial.distance**.

### ✅ **Cálculo Simples**
```python
import numpy as np

def manhattan_distance(p, q):
    return np.sum(np.abs(np.array(p) - np.array(q)))

# Exemplo
p = (2, 3)
q = (5, 7)
print("Distância de Manhattan:", manhattan_distance(p, q))  # Saída: 7
```

### ✅ **Usando `scipy`**
```python
from scipy.spatial.distance import cityblock

# Exemplo com Scipy
print("Distância de Manhattan (scipy):", cityblock(p, q))  # Saída: 7
```
🚀 **Nota:** `cityblock(p, q)` implementa diretamente a distância de Manhattan.

---

## 🔹 **Aplicação no KNN com Scikit-Learn**  
Podemos usar a distância de Manhattan no **K-Nearest Neighbors (KNN)** definindo o parâmetro `metric='manhattan'`.

### ✅ **KNN usando a Distância de Manhattan**
```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Criar o modelo KNN com distância de Manhattan
knn = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
knn.fit(X_train, y_train)

# Fazer previsões
y_pred = knn.predict(X_test)

# Avaliar a precisão
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")
```
---

## 🔹 **Comparação: Manhattan vs Euclidiana**
| Distância         | Fórmula                                              | Quando usar?                              |
|------------------|-----------------------------------------------------|------------------------------------------|
| **Euclidiana**   | \( \sqrt{\sum (x_i - y_i)^2} \)                     | Quando a diferença entre coordenadas é importante. |
| **Manhattan**    | \( \sum |x_i - y_i| \)                              | Quando o deslocamento ocorre em grade (ex: ruas de cidade). |

🔹 **Manhattan é menos sensível a outliers** porque não eleva as diferenças ao quadrado.  

---

## 🔹 **Conclusão**
A distância de Manhattan mede o deslocamento absoluto entre pontos e é útil quando os movimentos são restritos a direções ortogonais (como ruas). No **KNN**, ela pode melhorar a classificação quando as dimensões são independentes. 🚀