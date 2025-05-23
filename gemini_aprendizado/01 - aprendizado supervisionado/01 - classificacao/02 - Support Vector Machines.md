```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

# Etapa 1: Preparação dos Dados

# 1.1 Carregamento do Dataset
# Usamos o dataset 'iris' do scikit-learn, um dataset clássico para classificação.
iris = datasets.load_iris()
X = iris.data  # Features (características) das flores (comprimento e largura da sépala e pétala)
y = iris.target # Target (rótulos) das flores (0: setosa, 1: versicolor, 2: virginica)

# 1.2 Divisão em Treino e Teste
# Dividimos os dados em conjuntos de treino (70%) e teste (30%).
# O conjunto de treino é usado para treinar o modelo, e o de teste, para avaliar sua performance.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1.3 Escalonamento dos Dados (Normalização)
# SVMs são sensíveis à escala dos dados.  Escalonar os dados para que tenham média 0 e desvio padrão 1
# melhora a performance e a convergência do algoritmo.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train) # Ajusta o scaler aos dados de treino e transforma
X_test = scaler.transform(X_test)       # Aplica a transformação nos dados de teste (usa os parâmetros aprendidos no treino)

# Etapa 2: Treinamento do Modelo SVM

# 2.1 Criação e Configuração do Modelo SVM
# Criamos um objeto SVC (Support Vector Classifier).
#
# 'kernel': Especifica o tipo de kernel a ser usado no algoritmo.
#   - 'linear': Usa um kernel linear (útil para dados linearmente separáveis).
#   - 'rbf': Usa um kernel Radial Basis Function (RBF) (o mais comum, bom para dados não linearmente separáveis).
#   - 'poly': Usa um kernel polinomial.
#   - 'sigmoid': Usa um kernel sigmoidal.
# 'C': Parâmetro de regularização. Controla a penalidade por erros de classificação.
#   - Valores menores de C: Maior margem, mais erros de classificação permitidos (pode levar a underfitting).
#   - Valores maiores de C: Menor margem, menos erros de classificação permitidos (pode levar a overfitting).
# 'gamma': Coeficiente do kernel (necessário para 'rbf', 'poly' e 'sigmoid').
#   - 'scale' (padrão): gamma = 1 / (n_features * X.var())
#   - 'auto': gamma = 1 / n_features
#   - Um valor específico: influencia o raio de influência de cada ponto de suporte.
#     - Valores menores: Maior raio de influência (modelos mais generalistas).
#     - Valores maiores: Menor raio de influência (modelos mais complexos, com risco de overfitting).

svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')

# 2.2 Treinamento do Modelo
# Ajustamos o modelo SVM aos dados de treino.
svm_model.fit(X_train, y_train)

# Etapa 3: Avaliação do Modelo

# 3.1 Predições no Conjunto de Teste
# Usamos o modelo treinado para fazer predições sobre o conjunto de teste.
y_pred = svm_model.predict(X_test)

# 3.2 Cálculo da Acurácia
# A acurácia é a proporção de classificações corretas.
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")

# 3.3 Relatório de Classificação
# Fornece métricas detalhadas para cada classe (precisão, recall, f1-score, suporte).
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# 3.4 Matriz de Confusão
# Mostra a quantidade de amostras classificadas corretamente e incorretamente para cada classe.
cm = confusion_matrix(y_test, y_pred)
print("\nMatriz de Confusão:")
print(cm)

# 3.5 Visualização da Matriz de Confusão (opcional)
# Usamos seaborn para criar um heatmap da matriz de confusão para uma visualização mais clara.
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Matriz de Confusão")
plt.show()


# Etapa 4: Visualização da Decisão de Fronteira (Para visualização em 2D)
# (Esta parte é opcional e só funciona bem com 2 features)

# Reduzir o número de features para 2 para facilitar a visualização (opcional)
if X.shape[1] > 2:
  print("\nReduzindo o número de features para 2 para visualização...")
  X = X[:, :2] # Seleciona as duas primeiras features (comprimento e largura da sépala)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)
  svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
  svm_model.fit(X_train, y_train)
  y_pred = svm_model.predict(X_test)
  accuracy = accuracy_score(y_test, y_pred)
  print(f"Acurácia com 2 features: {accuracy:.2f}")


# Função para plotar a fronteira de decisão
def plot_decision_boundary(X, y, model, title="Fronteira de Decisão"):
    h = .02  # Tamanho do passo da malha
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

    # Plotar também os pontos de treinamento
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())


# Visualizar a fronteira de decisão (usando apenas as duas primeiras features)
if X.shape[1] == 2:
    plt.figure(figsize=(8, 6))
    plot_decision_boundary(X_train, y_train, svm_model)
    plt.show()

# Explicação Detalhada de Support Vector Machines (SVM)

# 1. Conceito Básico:
#   - SVM é um algoritmo de aprendizado supervisionado usado para classificação e regressão.
#   - A ideia principal é encontrar o hiperplano que melhor separa as classes no espaço de features.
#   - O "melhor" hiperplano é aquele que maximiza a margem entre as classes, onde a margem é a distância entre o hiperplano e os pontos de dados mais próximos de cada classe (os "vetores de suporte").

# 2. Hiperplano:
#   - Em um espaço bidimensional (2D), o hiperplano é uma linha.
#   - Em um espaço tridimensional (3D), o hiperplano é um plano.
#   - Em espaços de dimensões superiores, o hiperplano é uma generalização desses conceitos.
#   - O hiperplano divide o espaço de features em regiões que correspondem às diferentes classes.

# 3. Vetores de Suporte:
#   - São os pontos de dados mais próximos do hiperplano.
#   - A posição do hiperplano é influenciada diretamente pelos vetores de suporte.
#   - A remoção de outros pontos de dados não afeta o hiperplano, desde que os vetores de suporte permaneçam.

# 4. Margem:
#   - É a distância entre o hiperplano e os vetores de suporte.
#   - O objetivo do SVM é maximizar essa margem, o que geralmente leva a uma melhor generalização.

# 5. Kernel Trick:
#   - Permite que o SVM trabalhe com dados não linearmente separáveis.
#   - Transforma os dados originais em um espaço de dimensão superior onde eles se tornam linearmente separáveis.
#   - O kernel RBF (Radial Basis Function) é um dos kernels mais populares e é usado neste exemplo.
#   - Outros kernels incluem linear, polinomial e sigmoidal.

# 6. Regularização (Parâmetro C):
#   - Controla o compromisso entre maximizar a margem e minimizar os erros de classificação.
#   - Um valor de C pequeno resulta em uma margem maior, mas pode tolerar mais erros de classificação (underfitting).
#   - Um valor de C grande resulta em uma margem menor, mas tenta classificar todos os pontos corretamente (overfitting).

# 7. Gamma (Coeficiente do Kernel):
#   - Controla a influência de cada ponto de dados.
#   - Um valor de gamma pequeno significa que cada ponto de dados tem uma influência maior, o que leva a uma fronteira de decisão mais suave.
#   - Um valor de gamma grande significa que cada ponto de dados tem uma influência menor, o que leva a uma fronteira de decisão mais complexa e pode causar overfitting.

# 8. Vantagens do SVM:
#   - Eficaz em espaços de alta dimensão.
#   - Relativamente eficiente em termos de memória.
#   - Versátil: diferentes funções de Kernel podem ser especificadas para a função de decisão.

# 9. Desvantagens do SVM:
#   - Propenso a overfitting se o número de features for muito maior que o número de amostras.
#   - Pode ser computacionalmente caro para grandes datasets (complexidade cúbica no número de amostras no pior caso).
#   - A escolha do Kernel e dos parâmetros de regularização (C, gamma, etc.) pode ser difícil e requer experimentação.

# 10. Aplicações Comuns:
#   - Classificação de imagens.
#   - Reconhecimento de texto.
#   - Bioinformática (classificação de genes, proteínas).
#   - Detecção de fraudes.

# Resumo:

# Este script demonstra um exemplo prático de como usar SVM para classificação com o dataset Iris. Ele inclui a preparação dos dados, treinamento do modelo, avaliação e uma visualização da fronteira de decisão (com duas features). O código está bem comentado para facilitar a compreensão. As explicações detalhadas sobre SVM fornecem um entendimento mais profundo do algoritmo e seus parâmetros.
```

**Explicação Detalhada do Código:**

1.  **Importação das Bibliotecas:**

    *   `numpy`: Para operações numéricas.
    *   `matplotlib.pyplot`: Para plotar gráficos.
    *   `sklearn.datasets`: Para carregar o dataset Iris.
    *   `sklearn.model_selection`: Para dividir os dados em treino e teste.
    *   `sklearn.preprocessing`: Para escalar os dados (normalização).
    *   `sklearn.svm`: Para usar o algoritmo Support Vector Machine.
    *   `sklearn.metrics`: Para avaliar o modelo (acurácia, relatório de classificação, matriz de confusão).
    *   `seaborn`: Para visualização da matriz de confusão.

2.  **Preparação dos Dados:**

    *   **Carregamento do Dataset:** Carrega o dataset Iris, que contém informações sobre diferentes tipos de flores (Setosa, Versicolor, Virginica) com base em medidas de suas sépalas e pétalas.
    *   **Divisão em Treino e Teste:** Divide os dados em duas partes: um conjunto de treino (usado para treinar o modelo) e um conjunto de teste (usado para avaliar o desempenho do modelo em dados não vistos). `random_state` garante que a divisão seja a mesma cada vez que o código é executado, tornando os resultados reproduzíveis.
    *   **Escalonamento dos Dados (Normalização):**  SVMs são sensíveis à escala dos dados.  Escalonar os dados para que tenham média 0 e desvio padrão 1 melhora a performance e a convergência do algoritmo. O `StandardScaler` é usado para centralizar e dimensionar os dados.  É importante usar `fit_transform` *apenas* nos dados de treinamento.  Em seguida, o scaler treinado é usado para transformar os dados de teste, garantindo que a mesma transformação seja aplicada.

3.  **Treinamento do Modelo SVM:**

    *   **Criação e Configuração do Modelo:** Cria um objeto `SVC` (Support Vector Classifier) para classificação. O parâmetro `kernel` especifica o tipo de kernel a ser usado.  `rbf` é geralmente uma boa escolha padrão, pois funciona bem para dados não linearmente separáveis.  `C` é o parâmetro de regularização, e `gamma` é o coeficiente do kernel.
    *   **Treinamento do Modelo:** O método `fit` é usado para treinar o modelo com os dados de treino. O modelo aprende a relação entre as features e os rótulos no conjunto de treino.

4.  **Avaliação do Modelo:**

    *   **Predições no Conjunto de Teste:** O método `predict` é usado para fazer predições sobre o conjunto de teste.
    *   **Cálculo da Acurácia:** A acurácia é calculada comparando as predições do modelo com os rótulos reais no conjunto de teste.
    *   **Relatório de Classificação:** Fornece métricas mais detalhadas, como precisão, recall e f1-score para cada classe.
    *   **Matriz de Confusão:** Mostra o número de instâncias que foram classificadas corretamente e incorretamente para cada classe.  A matriz de confusão ajuda a entender quais classes estão sendo confundidas pelo modelo.
    *   **Visualização da Matriz de Confusão (Opcional):** Usa `seaborn` para criar um heatmap da matriz de confusão, o que facilita a visualização dos resultados.

5.  **Visualização da Fronteira de Decisão (Opcional):**

    *   **Redução de Features para 2:** Se o dataset tiver mais de 2 features, o código reduz para as duas primeiras features para permitir a visualização da fronteira de decisão.  Isto é *essencial* para que a função `plot_decision_boundary` funcione.
    *   **Função `plot_decision_boundary`:**  Cria uma grade de pontos e usa o modelo para prever a classe de cada ponto na grade. Em seguida, plota as regiões de decisão e os pontos de dados.
    *   **Plot da Fronteira de Decisão:** Chama a função `plot_decision_boundary` para visualizar a fronteira de decisão do modelo.

**Como Executar o Código:**

1.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install numpy matplotlib scikit-learn seaborn
    ```
2.  **Salve o código como um arquivo Python (por exemplo, `svm_example.py`).**
3.  **Execute o arquivo no terminal:**
    ```bash
    python svm_example.py
    ```

O código imprimirá a acurácia, o relatório de classificação, a matriz de confusão e, se tiver apenas duas features ou se a redução for feita, exibirá a fronteira de decisão.

**Dicas Adicionais:**

*   **Experimente com diferentes kernels:** Tente usar `kernel='linear'`, `kernel='poly'` ou `kernel='sigmoid'` e veja como isso afeta o desempenho do modelo.
*   **Ajuste os parâmetros `C` e `gamma`:**  Use técnicas como Grid Search ou Random Search para encontrar os melhores valores para esses parâmetros.
*   **Explore outros datasets:**  Tente usar outros datasets do scikit-learn ou seus próprios dados.
*   **Validação Cruzada:** Utilize validação cruzada (cross-validation) para obter uma estimativa mais robusta do desempenho do modelo.  Isto ajuda a mitigar o risco de overfitting nos dados de teste.

Este exemplo fornece uma base sólida para entender e usar SVM em seus próprios projetos de aprendizado de máquina.  Lembre-se de que a chave para um bom desempenho do SVM é a escolha cuidadosa do kernel e dos parâmetros de regularização, bem como uma preparação adequada dos dados.
