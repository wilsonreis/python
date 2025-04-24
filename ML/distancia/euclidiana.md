### 📌 **Distância Euclidiana: Entendimento Matemático e Aplicação no KNN em Python**  

A **distância Euclidiana** é a mais comum para medir a proximidade entre dois pontos em um espaço multidimensional. Ela é baseada no **Teorema de Pitágoras**, calculando a linha reta entre dois pontos.  

---

## 🔹 **Definição Matemática da Distância Euclidiana**  
Dada duas coordenadas \( P = (x_1, y_1) \) e \( Q = (x_2, y_2) \), a distância Euclidiana é definida como:

\[
D_{Euclidiana}(P, Q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

Em um espaço multidimensional (\( n \) dimensões), a fórmula se generaliza para:

\[
D_{Euclidiana}(P, Q) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
\]

---

## 🔹 **Exemplo Manual**  

Se tivermos os pontos \( P(2, 3) \) e \( Q(5, 7) \), então:

\[
D_{Euclidiana}(P, Q) = \sqrt{(5 - 2)^2 + (7 - 3)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
\]

---

## 🔹 **Implementação em Python**  

Podemos calcular a distância Euclidiana usando **NumPy** e **scipy.spatial.distance**.

### ✅ **Cálculo Simples**
```python
import numpy as np

def euclidean_distance(p, q):
    return np.sqrt(np.sum((np.array(p) - np.array(q))**2))

# Exemplo
p = (2, 3)
q = (5, 7)
print("Distância Euclidiana:", euclidean_distance(p, q))  # Saída: 5.0
```

### ✅ **Usando `scipy`**
```python
from scipy.spatial.distance import euclidean

# Exemplo com Scipy
print("Distância Euclidiana (scipy):", euclidean(p, q))  # Saída: 5.0
```
🚀 **Nota:** `euclidean(p, q)` implementa diretamente a distância Euclidiana.

---

## 🔹 **Aplicação no KNN com Scikit-Learn**  
A distância Euclidiana é a **métrica padrão** no **K-Nearest Neighbors (KNN)**.

### ✅ **KNN usando a Distância Euclidiana**
```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Criar o modelo KNN com distância Euclidiana (padrão)
knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)

# Fazer previsões
y_pred = knn.predict(X_test)

# Avaliar a precisão
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")
```
---

## 🔹 **Comparação: Euclidiana vs Manhattan**
| Distância         | Fórmula                                              | Quando usar?                              |
|------------------|-----------------------------------------------------|------------------------------------------|
| **Euclidiana**   | \( \sqrt{\sum (x_i - y_i)^2} \)                     | Quando as diferenças são relevantes e queremos medir a linha reta entre pontos. |
| **Manhattan**    | \( \sum |x_i - y_i| \)                              | Quando o deslocamento ocorre em eixos ortogonais (como ruas de cidade). |

🔹 **A Euclidiana é mais sensível a outliers** porque eleva as diferenças ao quadrado.

---

## 🔹 **Conclusão**
A distância Euclidiana mede a menor linha reta entre dois pontos e é amplamente usada em aprendizado de máquina, incluindo o **KNN**. Em **dados normalizados**, geralmente oferece melhores resultados do que a Manhattan. 🚀