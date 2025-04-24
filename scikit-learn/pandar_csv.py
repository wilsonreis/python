import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('vinho.csv')

# Supondo que a última coluna do seu CSV seja a variável target (y)
X = dados.iloc[:, :-1]  # Seleciona todas as colunas, exceto a última
y = dados.iloc[:, -1]   # Seleciona apenas a última coluna

# Divide os dados em conjuntos de treinamento e teste (80% para treino, 20% para teste)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando gráficos de dispersão
# Configurando o estilo do seaborn
sns.set_style("whitegrid")

# Criando uma figura com subplots para cada feature
n_features = X.shape[1]
fig, axes = plt.subplots(nrows=(n_features + 1) // 2, ncols=2, figsize=(15, 4 * ((n_features + 1) // 2)))
axes = axes.flatten()

# Plotando cada feature vs target
for i, coluna in enumerate(X.columns):
    sns.scatterplot(data=dados, x=coluna, y=y.name, ax=axes[i])
    axes[i].set_title(f'{coluna} vs {y.name}')

# Removendo subplots vazios se houver
for i in range(n_features, len(axes)):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.show()

# Agora você pode usar X_treino, X_teste, y_treino e y_teste
# para treinar e avaliar seus modelos do scikit-learn.
# Por exemplo, para treinar um modelo de Regressão Linear:
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_treino, y_treino)