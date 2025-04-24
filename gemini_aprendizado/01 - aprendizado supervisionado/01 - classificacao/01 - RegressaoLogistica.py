import numpy as np  # Importa a biblioteca NumPy para operações numéricas eficientes.
import pandas as pd  # Importa a biblioteca Pandas para manipulação e análise de dados.
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para visualização de dados.
from sklearn.model_selection import train_test_split  # Importa a função para dividir dados em treino e teste.
from sklearn.linear_model import LogisticRegression  # Importa o modelo de Regressão Logística.
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # Importa métricas de avaliação.
import seaborn as sns  # Importa a biblioteca Seaborn para visualização de dados estatísticos.

# **1. Preparação dos Dados:**

# Criando um DataFrame de exemplo (simulando dados de aprovação em um exame)
# Imagine que temos dados de alunos que fizeram um exame.
# 'horas_estudo': Quantidade de horas que o aluno estudou.
# 'aprovado': Se o aluno foi aprovado (1) ou não (0).

data = {'horas_estudo': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 1.5, 2.5, 3.5],
        'aprovado': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]}

df = pd.DataFrame(data)  # Cria um DataFrame Pandas com os dados.

# Exibindo as primeiras linhas do DataFrame para inspeção
print("Dados de Exemplo:\n", df.head())
print("\nInformações sobre os dados:\n", df.info())
print("\nEstatísticas descritivas:\n", df.describe())

# **2. Análise Exploratória (Opcional, mas recomendado):**

# Visualização dos dados para entender a relação entre as variáveis
plt.scatter(df['horas_estudo'], df['aprovado'], color='blue', label='Dados')  # Cria um gráfico de dispersão.
plt.xlabel('Horas de Estudo')  # Define o rótulo do eixo x.
plt.ylabel('Aprovado (0 ou 1)')  # Define o rótulo do eixo y.
plt.title('Horas de Estudo vs. Aprovação')  # Define o título do gráfico.
plt.legend()  # Mostra a legenda.
plt.grid(True)  # Adiciona um grid ao gráfico.
plt.show()  # Exibe o gráfico.

# Outro exemplo de visualização usando Seaborn
sns.regplot(x='horas_estudo', y='aprovado', data=df, logistic=True, ci=None)  # Mostra a relação entre horas de estudo e aprovação usando uma regressão logística.
plt.title('Regressão Logística: Horas de Estudo vs. Aprovação (Seaborn)')
plt.show()

# **3. Preparação dos Dados para o Modelo:**

# Definindo as variáveis independentes (X) e a variável dependente (y)
X = df[['horas_estudo']]  # Variável independente: horas de estudo.
y = df['aprovado']  # Variável dependente: aprovação (0 ou 1).

# Dividindo os dados em conjuntos de treino e teste
# Isso é crucial para avaliar o desempenho do modelo em dados não vistos.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# test_size=0.2 significa que 20% dos dados serão usados para teste, e 80% para treino.
# random_state=42 garante que a divisão seja a mesma sempre que o código for executado. Remove a aleatoriedade.

# **4. Criação e Treinamento do Modelo de Regressão Logística:**

# Inicializando o modelo de Regressão Logística
model = LogisticRegression()  # Cria uma instância do modelo.

# Treinando o modelo com os dados de treino
model.fit(X_train, y_train)  # Ajusta o modelo aos dados de treino. O modelo aprende a relação entre horas de estudo e aprovação.

# **5. Avaliação do Modelo:**

# Fazendo previsões com o conjunto de teste
y_pred = model.predict(X_test)  # Usa o modelo treinado para prever a aprovação para os dados de teste.

# Calculando a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)  # Compara as previsões com os valores reais e calcula a acurácia.
print("Acurácia do Modelo:", accuracy)

# Imprimindo o relatório de classificação (precisão, recall, f1-score, support)
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))
# Precisão: De todas as previsões positivas, quantas estavam corretas.
# Recall: De todos os valores positivos reais, quantos foram previstos corretamente.
# F1-score: Média harmônica entre precisão e recall.
# Support: Número de ocorrências de cada classe no conjunto de teste.

# Criando a matriz de confusão
cm = confusion_matrix(y_test, y_pred)
print("\nMatriz de Confusão:\n", cm)
# A matriz de confusão mostra:
# - Verdadeiros Positivos (TP): Quantas vezes o modelo previu corretamente que o aluno foi aprovado.
# - Verdadeiros Negativos (TN): Quantas vezes o modelo previu corretamente que o aluno não foi aprovado.
# - Falsos Positivos (FP): Quantas vezes o modelo previu que o aluno foi aprovado, mas ele não foi.
# - Falsos Negativos (FN): Quantas vezes o modelo previu que o aluno não foi aprovado, mas ele foi.

# Visualizando a matriz de confusão com Seaborn
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")  # Cria um mapa de calor da matriz de confusão.
plt.title('Matriz de Confusão')
plt.xlabel('Previsões')
plt.ylabel('Valores Reais')
plt.show()

# **6. Fazendo Previsões com Novos Dados:**

# Exemplo: Prever a probabilidade de aprovação para um aluno que estudou 6 horas
horas_estudo_novo = np.array([[6]])  # Cria um array NumPy com as horas de estudo.
probabilidade_aprovacao = model.predict_proba(horas_estudo_novo)[0, 1]  # Preve a probabilidade de aprovação.
print(f"\nProbabilidade de aprovação para 6 horas de estudo: {probabilidade_aprovacao:.2f}")
# .predict_proba retorna um array com duas colunas: a probabilidade de não aprovação e a probabilidade de aprovação.
# [0, 1] acessa a probabilidade de aprovação (segunda coluna) para a primeira amostra.
# .2f formata a probabilidade para mostrar apenas duas casas decimais.

# Exemplo: Prever se um aluno que estudou 6 horas será aprovado ou não
aprovado = model.predict(horas_estudo_novo)[0]  # Preve se o aluno será aprovado ou não.
print(f"Previsão de aprovação para 6 horas de estudo: {aprovado}")