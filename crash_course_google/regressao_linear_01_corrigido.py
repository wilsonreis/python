import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Dados
data = {'Libras em 1.000': [3.5, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37],
        'Milhas por galão': [18, 15, 18, 16, 15, 14, 24]}
df = pd.DataFrame(data)

# Criar e treinar o modelo
X = df[['Libras em 1.000']]
y = df['Milhas por galão']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Gerar dados para a linha de regressão
X_range = np.linspace(df['Libras em 1.000'].min(), df['Libras em 1.000'].max(), 100)
X_range = X_range.reshape(-1, 1)
y_range = model.predict(X_range)

# Plotar o gráfico
plt.scatter(df['Libras em 1.000'], df['Milhas por galão'])
plt.plot(X_range, y_range, color='red')
plt.xlabel('Libras em 1.000')
plt.ylabel('Milhas por galão')
plt.title('Regressão Linear de libras vs. milhas por galão')
plt.show()

# Avaliar o modelo (opcional)
from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Erro quadrático médio:', mse)
print('R-quadrado:', r2)