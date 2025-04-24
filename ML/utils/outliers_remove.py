import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy import stats

# Carrega o dataset Iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Adiciona a coluna target (espécie)
df['target'] = iris.target

# Visualização com boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.title('Boxplot do Dataset Iris')
plt.show()

# Identificação de outliers usando Z-score
z_scores = np.abs(stats.zscore(df.drop('target', axis=1)))
outliers = (z_scores > 3).any(axis=1)
print(f"Número de outliers encontrados (Z-score): {outliers.sum()}")

# Remoção de outliers
df_sem_outliers = df[~outliers]

# Visualização após a remoção
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_sem_outliers)
plt.title('Boxplot do Dataset Iris (sem outliers)')
plt.show()

# Identificação e tratamento de outliers por coluna
for col in df.columns[:-1]:  # Exclui a coluna 'target'
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    outliers_col = (df[col] < limite_inferior) | (df[col] > limite_superior)
    print(f"Número de outliers em {col}: {outliers_col.sum()}")

    # Trata os outliers substituindo por NaN (pode usar média, mediana, etc.)
    df.loc[outliers_col, col] = np.nan

# Preenche os NaNs com a mediana da coluna
df_tratado = df.fillna(df.median())

# Visualização após o tratamento por coluna
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_tratado)
plt.title('Boxplot do Dataset Iris (tratado por coluna)')
plt.show()