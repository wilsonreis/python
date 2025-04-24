def media_populacao(matriz):
    """
    Calcula a média aritmética de uma matriz 1 x n.

    Args:
        matriz (list): Uma lista contendo os valores da matriz.

    Returns:
        float: A média aritmética dos valores.
    """
    if not matriz or len(matriz) == 0:
        return 0  # Retorna 0 se a matriz estiver vazia

    soma = sum(matriz)  # Soma todos os elementos da matriz
    n = len(matriz)     # Número de elementos
    media = soma / n    # Calcula a média

    return media

def desvio_padrao(matriz):
    """
    Calcula o desvio padrão de uma matriz 1 x n.

    Args:
        matriz (list): Uma lista contendo os valores da matriz.

    Returns:
        float: O desvio padrão dos valores.
    """
    if not matriz or len(matriz) == 0:
        return 0  # Retorna 0 se a matriz estiver vazia

    media = media_populacao(matriz)  # Chama a função de média
    soma_quadrados = sum((x - media) ** 2 for x in matriz)  # Soma dos quadrados das diferenças
    n = len(matriz)  # Número de elementos
    desvio = (soma_quadrados / (n - 1)) ** 0.5  # Calcula o desvio padrão

    return desvio

