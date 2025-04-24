import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def generate_data(num_points=100):
    """Gera dados aleatórios para regressão linear."""
    X = np.linspace(0, 10, num_points)
    noise = np.random.normal(0, 2, num_points)
    y = 2 * X + 5 + noise
    return X.reshape(-1, 1), y

def train_and_predict(X, y):
    """Treina um modelo de regressão linear e faz previsões."""
    reg = linear_model.LinearRegression()
    reg.fit(X, y)
    y_pred = reg.predict(X)
    return reg, y_pred

def plot_regression(X, y, y_pred, title="Regressão Linear"):
    """Plota os dados e a linha de regressão."""
    plt.scatter(X, y)
    plt.plot(X, y_pred, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show()

def normalize_data(X_train, X_test):
    """Normaliza os dados usando MinMaxScaler."""
    scaler = MinMaxScaler()
    X_train_normalized = scaler.fit_transform(X_train)
    X_test_normalized = scaler.transform(X_test)
    return X_train_normalized, X_test_normalized

# --- Fluxo principal do programa ---
if __name__ == "__main__":
    # 1. Geração de dados
    X, y = generate_data()

    # 2. Treinamento e previsão
    reg, y_pred = train_and_predict(X, y)
    print("Coeficiente de inclinação (β1):", reg.coef_[0])
    print("Intercepto (β0):", reg.intercept_)

    # 3. Plotagem dos resultados
    plot_regression(X, y, y_pred)

    # 4. Normalização dos dados (apenas como exemplo,
    #    ajuste para seu caso de uso real)
    X_train = X[:80]  # Exemplo: usando 80% dos dados para treino
    X_test = X[80:]   # Exemplo: usando 20% dos dados para teste
    X_train_normalized, X_test_normalized = normalize_data(X_train, X_test)
    print("Dados de treino normalizados:\n", X_train_normalized[:5])
    print("Dados de teste normalizados:\n", X_test_normalized[:5])