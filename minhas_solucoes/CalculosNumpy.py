import numpy as np

class CalculosNumpy:
    def __init__(self, matriz):
        self.matriz = np.array(matriz)

    def media(self):
        """
        Calcula a média aritmética da matriz usando NumPy.

        Returns:
            float: A média aritmética dos valores.
        """
        return np.mean(self.matriz)

    def desvio_padrao(self):
        """
        Calcula o desvio padrão da matriz usando NumPy.

        Returns:
            float: O desvio padrão dos valores.
        """
        return np.std(self.matriz, ddof=1)  # ddof=1 para calcular o desvio padrão da amostra

    def erro_padrao(self):
        """
        Calcula o erro padrão da média usando NumPy.

        Returns:
            float: O erro padrão da média.
        """
        n = len(self.matriz)  # Número de observações
        if n <= 1:
            return float('nan')  # Retorna NaN se não houver dados suficientes
        return self.desvio_padrao() / np.sqrt(n)  # Erro padrão
