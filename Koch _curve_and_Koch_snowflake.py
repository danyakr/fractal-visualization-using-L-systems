import turtle


# Функция для установки координат черепашки
def set_turtle(t, my_tuple):
    t.up()
    t.goto(my_tuple[0], my_tuple[1])
    t.seth(my_tuple[2])
    t.down()


# Функция для генерация и отрисовки фрактала
def draw_koch_segment(t, ln):
    if ln > 6:
        ln3 = ln // 3
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
        t.right(120)
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)


t = turtle.Turtle()
t.ht()
t.speed(100)

set_turtle(t, (-200, -50, 0))

# Построение кривой Коха
draw_koch_segment(t, 120)

# Очистка экрана и перемещение черепашки
t.clear()
set_turtle(t, (-170, 100, 0))

# Построение снежинки Коха
draw_koch_segment(t, 120)
t.right(120)
draw_koch_segment(t, 120)
t.right(120)
draw_koch_segment(t, 120)

turtle.done()
