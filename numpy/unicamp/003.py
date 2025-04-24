import numpy as np

def imrprimir(matriz):
    print("-----------------------------------------------")
    print("Tipo do objeto:", type(matriz))
    print("Valor do objeto:", matriz)
    print("Número de dimensões do objeto:", matriz.ndim)
    print("Tamanho do objeto (número de elementos):", matriz.size)
    print("Forma do objeto (dimensões):", matriz.shape)

obj = np.arange(6)
imrprimir(obj)

obj = np.arange(10, 16)
imrprimir(obj)

obj = np.arange(10, 16, 2)
imrprimir(obj)


obj = np.arange(12)
imrprimir(obj)

obj = np.arange(12).reshape(3, 4)
imrprimir(obj)

obj = np.arange(12).reshape(2, 3, 2)
imrprimir(obj)




