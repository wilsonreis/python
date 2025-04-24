import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Supõe que perceptron_geeksforgeeks.py contém a classe Perceptron
try:
    from perceptron_geeksforgeeks import Perceptron  # Tenta importar
except ImportError:
    print("Erro: Arquivo perceptron_geeksforgeeks.py não encontrado.  Certifique-se de que ele está no mesmo diretório.")
    exit()

def train_and_evaluate_perceptron(num_samples=1000, test_size=0.2, num_epochs=100, random_state=23):
    """
    Gera dados, treina um Perceptron e avalia seu desempenho.

    Args:
        num_samples (int): Número de amostras no conjunto de dados.
        test_size (float): Proporção do conjunto de dados para usar para teste.
        num_epochs (int): Número de épocas para treinar o Perceptron.
        random_state (int): Seed para reprodutibilidade.

    Returns:
        None. Imprime a acurácia e plota os resultados.
    """

    # Generate a linearly separable dataset with two classes
    X, y = make_blobs(n_samples=num_samples,
                      n_features=2,
                      centers=2,
                      cluster_std=3,
                      random_state=random_state)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=test_size,
                                                        random_state=random_state,
                                                        shuffle=True)

    # Scale the input features to have zero mean and unit variance
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Set the random seed legacy
    np.random.seed(random_state)

    # Initialize the Perceptron with the appropriate number of inputs
    perceptron = Perceptron(num_inputs=X_train.shape[1])

    # Train the Perceptron on the training data
    perceptron.fit(X_train, y_train, num_epochs=num_epochs)

    # Prediction
    pred = perceptron.predict(X_test)

    # Test the accuracy of the trained Perceptron on the testing data
    accuracy = np.mean(pred != y_test)
    print("Accuracy:", accuracy)

    # Plot the dataset
    plt.scatter(X_test[:, 0], X_test[:, 1], c=pred)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

if __name__ == "__main__":
    train_and_evaluate_perceptron()