import turtle
from random import randint


class LSystem2D:
    def __init__(self, t, axiom, width, length, angle, color):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.t = t
        self.rules = {}
        self.color = color
        self.t.pensize(self.width)

    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def set_turtle(self, my_tuple):
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()

    def draw_turtle(self, start_pos, start_angle):
        turtle.tracer(1, 0)
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()
        turtle_stack = []

        for move in self.state:
            self.t.color(color)
            if move == 'F':
                self.t.forward(self.length)
            elif move == '@':
                self.length -= 4
                self.color[1] += 0.04
                self.width -= 2
                self.width = max(1, self.width)
                self.t.pensize(self.width)

            elif move == '+':
                self.t.left(self.angle())
            elif move == '-':
                self.t.right(self.angle())
            elif move == "[":
                turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize(), self.length, color[1]))
            elif move == "]":
                xcor, ycor, head, w, self.length, color[1] = turtle_stack.pop()
                self.set_turtle((xcor, ycor, head))
                self.width = w
                self.t.pensize(self.width)

        turtle.done()


width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
# screen.bgcolor("#191919")
screen.bgpic('img_1.png')

t = turtle.Turtle()
t.ht()

pen_width = 15
f_len = 50
color = [0.35, 0.2, 0.0]
angle = lambda: randint(0, 40)
axiom = 'A'

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle, color)
l_sys.add_rules(("A", "F[@[-A]+A]"))
l_sys.generate_path(11)
l_sys.draw_turtle((0, -200), 90)
