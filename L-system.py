import sys
import turtle


# Функция для установки начальной позиции черепашки
def set_value(rot, x, y):
    global rotate
    global x_coord
    global y_coord

    rotate = rot
    x_coord = x
    y_coord = y


class LSystem2D:
    """Класс для работы с L-системами.

    Атрибуты:
        axiom (str): Аксиома.
        state (str): Текущее состояние системы.
        width (int): Ширина линии.
        length (int): Длина линейного сегмента кривой.
        angle (int): Угол поворота.
        t (Turtle): Ссылка на объект черепашки.
        rules (dict): Словарь для хранения правил формирования кривых.
    """

    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.t = t
        self.rules = {}
        self.t.pensize(self.width)

    def add_rules(self, *rules):
        """Добавляет правило в словарь.

        Args:
            *rules(tuple): Правила в формате (ключ, значение).
        """
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        """Генерирует строку символов на нужной итерации (маршрут для черепашки).

        Args:
            n_iter(int): Номер итерации.
        """
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def set_turtle(self, my_tuple):
        """Устанавливает позицию черепашки.

        Args:
            my_tuple (tuple): Позиция черепашки в формате (x, y, угол).
        """
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()

    def draw_turtle(self, start_pos, start_angle):
        """Отрисовывает фрактал с помощью черепашки (обрабатывает строку символов).

            F: движение вперед на длину lenght
            G: движение вперед на длину lenght
            A: движение вперед и поворот влево
            B: движение вперед и поворот вправо
            +: поворот влево на угол angle
            -: поворот вправо на угол angle
            [: сохранение текущего состояния черепашки в стек
            ]: восстановление сохраненного состояния черепашки из стека

            Args:
                start_pos (tuple): Начальная позиция черепашки.
                start_angle (int): Начальный угол поворота черепашки.
            """
        turtle.tracer(1, 0)
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()
        turtle_stack = []

        for move in self.state:
            if move == 'F':
                self.t.forward(self.length)
            elif move == 'G':
                self.t.forward(self.length)
            elif move == 'A':
                self.t.forward(self.length)
                self.t.left(self.angle)
            elif move == 'B':
                self.t.forward(self.length)
                self.t.right(self.angle)
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)
            elif move == "[":
                turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize()))
            elif move == "]":
                xcor, ycor, head, w = turtle_stack.pop()
                self.set_turtle((xcor, ycor, head))
                self.width = w
                self.t.pensize(self.width)

        turtle.done()


set_value(0, -200, 0)

flag = True
while flag:

    print('\nВыберите группу фракталов:\n')
    print('\t1. Простейшие фракталы\n'
          '\t2. Усложненные фракталы\n'
          '\t3. Деревья\n'
          '\t4. Другое\n'
          '\t5. Завершение\n')

    num = int(input('Введите цифру: '))

    if num == 1:
        while flag:
            print('\nВыберите фрактал:\n')
            print('\t1. Кривая Коха\n'
                  '\t2. Снежинка Коха\n'
                  '\t3. С-Кривая Леви\n'
                  '\t4. П-Кривая Леви\n'
                  '\t5. Остров Леви\n'
                  '\t6. Назад\n')

            num = int(input('Введите цифру: '))

            if num == 1:
                angle = 60
                axiom = "F"
                rules = (("F", "F+F--F+F"),)
                flag = False

            if num == 1: continue  # Чтобы не печаталось else: print('Выберите пункт меню') в коцне цикла

            elif num == 2:
                angle = 60
                axiom = "F--F--F"
                rules = (("F", "F+F--F+F"),)
                flag = False

            if num == 2: continue  # Чтобы не печаталось else: print('Выберите пункт меню') в коцне цикла

            elif num == 3:
                angle = 45
                axiom = "F"
                rules = (("F", "+F--F+"),)
                flag = False

            if num == 4:
                angle = 45
                axiom = "++FF--F--FF++"
                rules = (("F", "+F--F+"),)
                flag = False

            if num == 5:
                angle = 45
                axiom = "F--F--F--F"
                rules = (("F", "+F--F+"),)
                flag = False

            elif num == 6:
                break

            else:
                print('Выберите пункт меню')

    elif num == 2:
        while flag:
            print('\nВыберите фрактал:\n')
            print('\t1. Дракон Хартера-Хайтвея\n'
                  '\t2. Треугольник Серпинского\n'
                  '\t3. Назад\n')

            num = int(input('Введите цифру: '))

            if num == 1:
                angle = 90
                axiom = 'FX'
                rules = (("X", "X+YF+"), ("Y", "-FX-Y"), )
                flag = False

            elif num == 2:
                angle = 120
                axiom = 'F+G+G'
                rules = (("F", "F+G-F-G+F"), ("G", "GG"), )
                flag = False

            elif num == 3:
                break
            else:
                print('Выберите пункт меню')

    elif num == 3:
        while flag:
            print('\nВыберите фрактал:\n')
            print('\t1. Дерево 1\n'
                  '\t2. Дерево 2\n'
                  '\t3. Дерево Пифагора\n'
                  '\t4. Растение 1\n'
                  '\t5. Растение 2\n'
                  '\t6. Растение 3\n'
                  '\t7. Растение 4\n'
                  '\t8. Назад\n')

            num = int(input('Введите цифру: '))

            if num == 1:
                angle = int(input('Задайте угол (чтобы использовать по умолчанию угол 30 градусов нажмите Enter): ') or 30)
                axiom = 'F'
                rules = (("F", "F[+F][-F]"), )
                set_value(90, 0, -250)
                flag = False

            elif num == 2:
                angle = int(input('Задайте угол (чтобы использовать по умолчанию угол 30 градусов нажмите Enter): ') or 30)
                axiom = 'A'
                rules = (("A", "F[+A][-A]"), ("F", "FF"), )
                set_value(90, 0, -250)
                flag = False

            elif num == 3:
                angle = 45
                axiom = 'A'
                rules = (("A", "F[+A][-A]"), ("F", "FF"),)
                set_value(90, 0, -250)
                flag = False

            elif num == 4:
                angle = int(input('Задайте угол (чтобы использовать по умолчанию угол 30 градусов нажмите Enter): ') or 30)
                axiom = 'A'
                rules = (("A", "F[+A]F[-A]+A"), ("F", "FF"),)
                set_value(90, 0, -250)
                flag = False

            elif num == 5:
                angle = int(input('Задайте угол (чтобы использовать по умолчанию угол 30 градусов нажмите Enter): ') or 30)
                axiom = 'A'
                rules = (("A", "F[+A][-A]F+A"), ("F", "FF"),)
                set_value(90, 0, -250)
                flag = False

            elif num == 6:
                angle = int(input('Задайте угол (чтобы использовать по умолчанию угол 30 градусов нажмите Enter): ') or 30)
                axiom = 'A'
                rules = (("A", "F[+A]F[-A]F+A"), ("F", "FF"),)
                set_value(90, 0, -250)
                flag = False

            elif num == 7:
                angle = int(input('Задайте угол (чтобы использовать по умолчанию угол 25 градусов нажмите Enter): ') or 25)
                axiom = 'X'
                rules = (("X", "F+[[X]-X]-F[-FX]+X"), ("F", "FF"),)
                set_value(90, 0, -250)
                flag = False

            elif num == 8:
                break
            else:
                print('Выберите пункт меню')

    elif num == 4:
        while flag:
            print('\nВыберите пункт:\n')
            print('\t1. Моделирование роста водорослей\n'
                  '\t2. Задать свою систему (возможно только использование символов F, G, A, B, +, -, [, ])\n'
                  '\t3. Назад\n')

            num = int(input('Введите цифру: '))

            if num == 1:
                angle = 60
                axiom = "A"
                rules = (("A", "AB"), ("B", "A"), )
                flag = False

            elif num == 2:
                angle = int(input('Введите угол (в градусах): '))
                axiom = input('Введите аксиому: ')
                print('Введите правила')

                rules = []

                while True:
                    symbol = input('Введите символ, чтобы закончить ввод просто нажмите Enter: ')
                    if not symbol:
                        break

                    replacement = input('Во что преобразовать символ: ')
                    if not replacement:
                        break

                    rules.append((symbol, replacement))

                rules = tuple(rules)

                flag = False

            elif num == 3:
                break
            else:
                print('Выберите пункт меню')

    elif num == 5:
        print('Завершение')
        sys.exit()

    else:
        print('Выберите пункт меню')

gen = int(input('Введите поколение (итерацию) фрактала '
                '(не рекомендуется вводить больше 15, оптимально 7-10, быстро 3-7, по умолчанию 5):') or 5)

width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
# screen.bgcolor("#191919")
# screen.bgpic('img_4.png')

t = turtle.Turtle()
t.ht()

# t.color('#96A632')
# pen_width = 1
# f_len = 10
pen_width = int(input('Введите толщину линии:'))
f_len = int(input('Введите длину линейного участка:'))

# angle = 25
# axiom = 'X'

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rules(("F", "F+G-F-G+F"), ("G", "GG"))
l_sys.add_rules(*rules)
l_sys.generate_path(gen)
l_sys.draw_turtle((x_coord, y_coord), rotate)
