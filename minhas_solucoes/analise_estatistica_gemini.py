import numpy as np


class AnaliseEstatistica:
    """
    Classe para calcular estatísticas básicas de uma matriz 1xn usando NumPy.

    Atributos:
        matriz (numpy.ndarray): A matriz 1xn de dados.  Deve ser um array NumPy.

    Métodos:
        calcular_media(): Calcula a média aritmética da matriz.
        calcular_desvio_padrao(): Calcula o desvio padrão da matriz.
        calcular_erro_padrao(): Calcula o erro padrão da média da matriz.
    """

    def __init__(self, matriz):
        """
        Construtor da classe AnaliseEstatistica.

        Args:
            matriz (list ou numpy.ndarray): A matriz 1xn de dados.
                Se uma lista for passada, ela será convertida em um array NumPy.

        Raises:
            TypeError: Se a entrada não for uma lista ou um array NumPy.
            ValueError: Se a matriz não for 1xn (ou seja, não tiver uma única linha).
        """
        if not isinstance(matriz, (list, np.ndarray)):
            raise TypeError("A entrada deve ser uma lista ou um array NumPy.")

        if isinstance(matriz, list):
            matriz = np.array(matriz)

        if matriz.ndim != 1:
            raise ValueError("A matriz deve ser 1xn (ou seja, um array unidimensional).")

        self.matriz = matriz

    def calcular_media(self):
        """
        Calcula a média aritmética da matriz.

        Returns:
            float: A média aritmética dos dados.
        """
        return np.mean(self.matriz)

    def calcular_desvio_padrao(self):
        """
        Calcula o desvio padrão da matriz.

        Returns:
            float: O desvio padrão dos dados.
        """
        return np.std(self.matriz, ddof=1)

    def calcular_erro_padrao(self):
        """
        Calcula o erro padrão da média da matriz.

        Returns:
            float: O erro padrão da média dos dados.
        """
        desvio_padrao = self.calcular_desvio_padrao()
        tamanho_amostra = len(self.matriz)
        return desvio_padrao / np.sqrt(tamanho_amostra)


# Exemplo de uso:
if __name__ == '__main__':
    # Dados de exemplo
    dados = [4, 8, 6, 5, 3]

    # Cria um objeto da classe
    analise = AnaliseEstatistica(dados)

    # Calcula e imprime as estatísticas
    media = analise.calcular_media()
    desvio_padrao = analise.calcular_desvio_padrao()
    erro_padrao = analise.calcular_erro_padrao()

    print(f"Média: {media}")
    print(f"Desvio Padrão: {desvio_padrao}")
    print(f"Erro Padrão da Média: {erro_padrao}")

    # Exemplo com NumPy array
    dados_np = np.array([10, 20, 30, 40, 50])
    analise_np = AnaliseEstatistica(dados_np)

    print("\nCom NumPy array:")
    print(f"Média: {analise_np.calcular_media()}")
    print(f"Desvio Padrão: {analise_np.calcular_desvio_padrao()}")
    print(f"Erro Padrão da Média: {analise_np.calcular_erro_padrao()}")

    # Exemplo de tratamento de erro
    try:
        analise_erro = AnaliseEstatistica([[1, 2], [3, 4]])  # Matriz 2x2 (inválida)
    except ValueError as e:
        print(f"\nErro ao criar objeto: {e}")

    try:
        analise_erro = AnaliseEstatistica("string")  # Tipo inválido
    except TypeError as e:
        print(f"\nErro ao criar objeto: {e}")