from minhas_solucoes.CalculosNumpy import CalculosNumpy

# Exemplo de uso da classe CalculosNumpy
valores = [4, 8, 6, 5, 3]
calculos_numpy = CalculosNumpy(valores)

media_numpy = calculos_numpy.media()
desvio_numpy = calculos_numpy.desvio_padrao()
erro_padrao_numpy = calculos_numpy.erro_padrao()

print("A média aritmética (NumPy) é:", media_numpy)
print("O desvio padrão (NumPy) é:", desvio_numpy)
print("O erro padrão (NumPy) é:", erro_padrao_numpy)