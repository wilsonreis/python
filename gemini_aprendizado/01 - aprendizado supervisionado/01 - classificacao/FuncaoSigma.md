## Função Sigmoide (Função Logística) 

<p align="center"> <img width="350px" src="Função Sigmoide.bmp" alt="Erro Padrão"> </p>

# σ(z) = 1 / (1 + exp(-z))

A função sigmoide, também conhecida como função logística, é uma função matemática que produz uma curva em forma de "S". Ela é amplamente utilizada em diversas áreas, incluindo estatística, redes neurais e aprendizado de máquina, devido às suas propriedades importantes e úteis.

**Detalhes da Função:**

*   **Definição:** A função sigmoide é definida pela fórmula:

    σ(z) = 1 / (1 + exp(-z))

    onde:
    *   `σ(z)` é o valor da função sigmoide para a entrada `z`.
    *   `z` é a entrada da função (pode ser qualquer número real).
    *   `exp(z)` é a função exponencial (e elevado à potência de z).

    
*   **Significado:** 
    * Essa fórmula "espreme" qualquer valor `z` entre 0 e 1.  Valores muito grandes de `z` se aproximam de 1 (alta probabilidade), valores muito pequenos de `z` se aproximam de 0 (baixa probabilidade), e `z = 0` resulta em uma probabilidade de 0.5.

*   **Domínio e Imagem:**
    *   O domínio da função sigmoide é todos os números reais (-∞, +∞).
    *   A imagem da função sigmoide é o intervalo aberto (0, 1). Ou seja, o valor da função sempre estará entre 0 e 1, nunca atingindo esses valores.

*   **Propriedades:**
    *   **Contínua e Diferenciável:** A função sigmoide é contínua e diferenciável em todo o seu domínio.
    *   **Monotonicamente Crescente:** A função sigmoide é monotonicamente crescente, o que significa que à medida que o valor de `z` aumenta, o valor de `σ(z)` também aumenta.
    *   **Assíntotas Horizontais:** A função sigmoide possui duas assíntotas horizontais:
        *   `σ(z)` se aproxima de 0 quando `z` tende a -∞.
        *   `σ(z)` se aproxima de 1 quando `z` tende a +∞.
    *   **Ponto de Inflexão:** A função sigmoide tem um ponto de inflexão em `z = 0`, onde a concavidade da curva muda. No ponto de inflexão, `σ(0) = 0.5`.
    *   **Simetria:** A função sigmoide é simétrica em relação ao ponto (0, 0.5). Isso significa que `σ(-z) = 1 - σ(z)`.
    *   **Derivada:** A derivada da função sigmoide é dada por:

        σ'(z) = σ(z) * (1 - σ(z))

        Essa propriedade é particularmente útil em algoritmos de aprendizado de máquina, como o backpropagation.

**Importância e Aplicações:**

*   **Estatística:** A função sigmoide é usada em regressão logística para modelar a probabilidade de um evento ocorrer.
*   **Redes Neurais:** A função sigmoide é frequentemente utilizada como função de ativação em neurônios artificiais, introduzindo não linearidade no modelo e permitindo que a rede aprenda padrões complexos.
*   **Aprendizado de Máquina:** Em geral, a função sigmoide é usada para mapear valores em um intervalo entre 0 e 1, o que é útil para problemas de classificação e para representar probabilidades.
*   **Outras áreas:** A função sigmoide também aparece em modelos de crescimento populacional, processos de decisão e outros fenômenos naturais.

**Vantagens de usar a função sigmoide:**

*   **Saída Limitada:** A saída da função está sempre entre 0 e 1, o que facilita a interpretação como uma probabilidade.
*   **Diferenciabilidade:** A diferenciabilidade da função é crucial para algoritmos de otimização baseados em gradiente, como o backpropagation.
*   **Não Linearidade:** A função introduz não linearidade no modelo, permitindo que ele aprenda relações complexas nos dados.

**Desvantagens de usar a função sigmoide:**

*   **Problema do Desaparecimento do Gradiente:** Em redes neurais profundas, o gradiente pode se tornar muito pequeno à medida que se propaga para as camadas anteriores, dificultando o treinamento da rede. Isso ocorre porque a derivada da função sigmoide se aproxima de zero para valores muito grandes ou muito pequenos de `z`.
*   **Não Centralizada em Zero:** A saída da função sigmoide não é centralizada em zero, o que pode levar a um aprendizado mais lento em algumas situações.

**Código Python para gerar o gráfico da função sigmoide:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Define a função sigmoide
def sigmoid(z):
  """Calcula a função sigmoide."""
  return 1 / (1 + np.exp(-z))

# Cria um array de valores para o eixo x (z)
z = np.linspace(-10, 10, 400) # Gera 400 pontos entre -10 e 10

# Calcula os valores correspondentes da função sigmoide
sigma_z = sigmoid(z)

# Cria o gráfico
plt.figure(figsize=(8, 6))  # Ajusta o tamanho da figura
plt.plot(z, sigma_z, label='σ(z) = 1 / (1 + exp(-z))')

# Adiciona título e rótulos aos eixos
plt.title('Função Sigmoide')
plt.xlabel('z')
plt.ylabel('σ(z)')

# Adiciona uma grade para facilitar a visualização
plt.grid(True)

# Adiciona a legenda
plt.legend()

# Adiciona linhas horizontais em y=0 e y=1
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.axhline(1, color='black', linestyle='--', linewidth=0.5)

# Adiciona linha vertical em x=0
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)

# Mostra o gráfico
plt.show()
```

**Explicação do código:**

1.  **Importa as bibliotecas:**
    *   `numpy` é usado para criar arrays e realizar cálculos numéricos eficientes.
    *   `matplotlib.pyplot` é usado para criar o gráfico.

2.  **Define a função sigmoide:**
    *   A função `sigmoid(z)` recebe um valor `z` como entrada e retorna o valor da função sigmoide para esse valor.

3.  **Cria um array de valores para o eixo x (z):**
    *   `np.linspace(-10, 10, 400)` cria um array com 400 valores igualmente espaçados entre -10 e 10.  Esses valores serão usados como entrada para a função sigmoide e representam o eixo horizontal do gráfico.

4.  **Calcula os valores correspondentes da função sigmoide:**
    *   `sigma_z = sigmoid(z)` aplica a função `sigmoid` a cada elemento do array `z` e armazena os resultados no array `sigma_z`.  Estes valores representam o eixo vertical do gráfico.

5.  **Cria o gráfico:**
    *   `plt.figure(figsize=(8, 6))` cria uma nova figura com um tamanho específico (largura 8 polegadas, altura 6 polegadas).  Ajustar o tamanho da figura pode melhorar a legibilidade do gráfico.
    *   `plt.plot(z, sigma_z, label='σ(z) = 1 / (1 + exp(-z))')` plota os pontos `(z, sigma_z)` e adiciona uma legenda para identificar a curva.
    *   `plt.title('Função Sigmoide')` define o título do gráfico.
    *   `plt.xlabel('z')` define o rótulo do eixo x.
    *   `plt.ylabel('σ(z)')` define o rótulo do eixo y.
    *   `plt.grid(True)` adiciona uma grade ao gráfico para facilitar a leitura dos valores.
    *   `plt.legend()` mostra a legenda do gráfico.
    *   `plt.axhline(0, color='black', linestyle='--', linewidth=0.5)` e `plt.axhline(1, color='black', linestyle='--', linewidth=0.5)` adicionam linhas horizontais tracejadas em y=0 e y=1 para destacar as assíntotas.
    *   `plt.axvline(0, color='black', linestyle='--', linewidth=0.5)` adiciona uma linha vertical tracejada em x=0 para destacar o ponto de inflexão.

6.  **Mostra o gráfico:**
    *   `plt.show()` exibe o gráfico na tela.

Ao executar este código, você verá um gráfico da função sigmoide, mostrando sua forma de "S" característica, o intervalo de valores entre 0 e 1, e as assíntotas horizontais.

Em resumo, a função sigmoide é uma ferramenta poderosa com diversas aplicações. Compreender suas propriedades e limitações é essencial para utilizá-la de forma eficaz.
