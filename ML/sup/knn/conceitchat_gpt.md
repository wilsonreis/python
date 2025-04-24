### K-Nearest Neighbors (KNN) no Machine Learning  

O **K-Nearest Neighbors (KNN)** é um algoritmo de aprendizado supervisionado usado para **classificação** e **regressão**. Ele funciona baseando-se na proximidade de um dado em relação aos seus vizinhos mais próximos no espaço multidimensional.

---

### 🔹 Como Funciona o KNN?
1. **Definir o valor de K**: Escolher um número "K" de vizinhos mais próximos.
2. **Calcular a distância**: Para cada novo dado, calcular a distância entre ele e os dados de treinamento (geralmente usando distância Euclidiana).
3. **Selecionar os K vizinhos mais próximos**: Identificar os "K" pontos mais próximos ao novo dado.
4. **Classificação ou Regressão**:
   - **Classificação**: A classe mais frequente entre os K vizinhos é atribuída ao novo ponto.
   - **Regressão**: A média dos valores dos K vizinhos é usada como a previsão.

---

### 🔹 Principais Características:
✅ **Simplicidade**: Fácil de entender e implementar.  
✅ **Não-paramétrico**: Não faz suposições sobre a distribuição dos dados.  
✅ **Baseado em Instâncias**: Armazena todos os dados de treinamento, não há fase explícita de "treinamento".  

---

### 🔹 Vantagens:
✔️ Bom desempenho para **pequenos conjuntos de dados**.  
✔️ Pode se adaptar a **dados não-lineares**.  
✔️ **Intuitivo** e fácil de interpretar.  

---

### 🔹 Desvantagens:
❌ **Lento para grandes volumes de dados**, pois precisa calcular a distância para todos os pontos.  
❌ **Sensível a ruídos** e valores atípicos.  
❌ **A escolha de K** pode afetar o desempenho.  

---

### 🔹 Aplicações do KNN:
📌 **Reconhecimento de padrões** (ex: reconhecimento facial).  
📌 **Sistemas de recomendação**.  
📌 **Análise de crédito**.  
📌 **Diagnóstico médico** (ex: detecção de doenças com base em sintomas).  

---

### 🔹 Exemplo Prático em Python:
```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar o dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Criar e treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Fazer previsões
y_pred = knn.predict(X_test)

# Avaliar o modelo
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")
```

---

### 🔹 Como Escolher o Melhor K?
- **Valores pequenos de K** (ex: K=1, K=3) podem levar a **overfitting**.  
- **Valores grandes de K** (ex: K=15, K=20) podem tornar o modelo muito **generalista**.  
- Uma abordagem comum é testar diferentes valores de K e escolher o que apresenta **melhor desempenho na validação cruzada**.  

---

### 🔹 Conclusão:
O KNN é um algoritmo poderoso para problemas simples de classificação e regressão, mas pode ser ineficiente para grandes bases de dados. A escolha do número de vizinhos (K) e da métrica de distância é essencial para um bom desempenho. 🚀