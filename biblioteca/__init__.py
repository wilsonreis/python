import numpy as np

def main():
    imprimir(np.arange(6))

def imprimir(matriz):
    print("-----------------------------------------------")
    print("Tipo do objeto:", type(matriz))
    print("Valor do objeto:", matriz)
    print("Número de dimensões do objeto:", matriz.ndim)
    print("Tamanho do objeto (número de elementos):", matriz.size)
    print("Forma do objeto (dimensões):", matriz.shape)

if __name__ == '__main__':
    main()