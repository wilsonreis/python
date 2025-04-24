# Importa a biblioteca turtle, que permite criar gráficos simples
import turtle

# Cria uma janela gráfica onde as operações serão executadas
wn = turtle.Screen()
#wn.setup(width=1024, height=600)
wn.setup(width=800, height=600, startx=0, starty=0)
# Cria uma tartaruga chamada alex, que será usada para desenhar na janela
alex = turtle.Turtle()


# Move a tartaruga alex para frente, desenhando uma linha de 150 unidades
alex.forward(150)

# Gira a tartaruga alex 90 graus para a esquerda
alex.left(90)

# Move a tartaruga alex para frente, desenhando outra linha de 75 unidades
alex.forward(75)

# Aguarda o clique do mouse para fechar a janela gráfica
wn.exitonclick()