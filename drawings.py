import turtle

# Рисуем движущийся кружок
turtle.shape("circle")
# Рисуем белый круг с черным контуром
turtle.color("black", "white")

# Направляем шарик наверх экрана на 300 пикселей
turtle.speed(0)
turtle.penup()
turtle.goto(0, 300)

# Поворачиваем шарик вправо под углом 40 градусов, оставляя след
turtle.pendown()
turtle.stamp()
turtle.right(40)
turtle.speed(1)

# Направляем шарик вперед
turtle.speed(0)
for _ in range(4):
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.forward(33)
    turtle.pendown()

# Рисуем полукруг
turtle.circle(-80, 100)

# Направляем шарик вперед
for _ in range(4):
    turtle.penup()
    turtle.forward(33)
    turtle.pendown()
    turtle.forward(50)

# Оставляем след
turtle.stamp()

# Направляем шарик на 200 пикселей вперед и поворачиваем шарик вправо на 130 градусов
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.right(130)

# Направляем шарик вперед
for _ in range(3):
    turtle.pendown()
    turtle.forward(45)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

# Оставляем след и поворачиваем шарик на 90 градусов влево
turtle.stamp()
turtle.left(90)

# Направляем шарик вперед
for _ in range(3):
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
