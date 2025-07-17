import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

def desenha_flor(turtle_obj, tamanho, cor):
    turtle_obj.color(cor)
    turtle_obj.begin_fill()
    for _ in range(6):  # 6 pétalas
        turtle_obj.circle(tamanho, 60)
        turtle_obj.left(120)
        turtle_obj.circle(tamanho, 60)
        turtle_obj.left(60)
    turtle_obj.end_fill()

def vai_para(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

cores = ["red", "yellow", "blue", "orange", "pink", "purple", "white", "cyan", "magenta"]

# desenha 10 flores em posições aleatórias
for _ in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    vai_para(x, y)
    cor = random.choice(cores)
    desenha_flor(t, 20, cor)

# escreve no centro
vai_para(0, -250)
t.color("white")
t.write("aaaaaaaaaaaa", align="center", font=("Arial", 48, "bold"))

t.hideturtle()
turtle.done()
