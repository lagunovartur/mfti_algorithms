import turtle as m_turtle
import math

turtle = m_turtle.Turtle()
turtle.speed(5)
turtle.shape('turtle')


def draw_s(l: float = 30):
    '''
    Упражнение 2.

    Рисует букву S.

    :param l: float, длинна стороны буквы S.
    '''

    turtle.shape('turtle')
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(l)


def draw_square(l: float = 100):
    '''
    Упражнение 3.

    Рисует квадрат.

    :param l: float, длина стороны квадрата.
    '''

    for i in range(4):
        turtle.forward(l)
        turtle.left(90)


def draw_circle(r: float = 50):
    '''
    Упражнение 4.

    Рисует круг.

    :param r: float, радиус круга.
    '''

    length = 2 * math.pi * r
    angle = 360

    for i in range(angle):
        turtle.forward(length / angle)
        turtle.left(1)


def draw_nested_squares(n: int = 10, inc: float = 20):
    '''
    Упражнение 5.

    Рисует вложенные квадраты.

    :param n: int, количество квадратов.
    :param inc: float, приращение стороны квадрата.
    '''

    next_position = [0, 0]
    c_l = inc

    for i in range(n):
        draw_square(c_l)
        c_l += inc * 2
        next_position[0] -= inc
        next_position[1] -= inc
        turtle.penup()
        turtle.goto(next_position[0], next_position[1])
        turtle.pendown()


def draw_spider(n: int = 10, l: float = 100):
    '''
    Упражнение 6.

    Рисует паука.

    :param n: int, количество лап паука.
    :param l: float, длина лапы паука.
    '''

    for i in range(n):
        turtle.forward(l)
        turtle.stamp()
        turtle.backward(l)
        turtle.left(360 / n)


def draw_round_spiral(l:int = 1000):
    '''
    Упражнение 7.

    Рисует круглую спираль.

    :param l: Длина спирали в пикселях.
    '''

    for i in range(l):
        turtle.forward(i * 0.001)
        turtle.left(1)


def draw_square_spiral(n: int = 50, inc: float = 10):
    '''
    Упражнение 8.

    Рисует квадратную спираль.

    :param n: int, количество сторон спирали.
    :param inc: float, приращение стороны спирали.
    '''

    c_l = inc

    for i in range(n):
        turtle.forward(c_l)
        turtle.left(90)

        turtle.forward(c_l)
        turtle.left(90)

        c_l += inc


def draw_regular_polygons(n: int = 12, s_l: float = 50, inc: float = 20):
    '''
    Упражнение 9.
    Функция рисует вложенные правильные многоугольники.

    :param n: int, количество сторон максимального многоугольника
    :param s_l: float, начальная длина стороны первого многоугольника
    :param inc: float, приращение длинны описываемой окружности
    '''

    c_l = s_l
    c_r = c_l / (2 * math.sin(math.radians(360 / (2 * 3))))

    for i in range(3, n + 1):

        o_a = 0
        s_a = abs(360 / (2 * i) - 90)
        turtle.left(s_a)
        o_a += s_a
        c_a = 360 / i

        for j in range(i):
            o_a += c_a
            o_a = o_a % 360
            turtle.left(c_a)
            turtle.forward(c_l)

        turtle.right(o_a)
        o_a = 0

        turtle.penup()
        turtle.forward(inc)
        turtle.pendown()

        c_r += inc
        c_l = c_r * 2 * math.sin(math.radians(360/(2*(i + 1))))


def draw_flower(n: int = 6, r: float = 50):
    '''
    Упражнение 10.

    Рисует цветок.

    :param n: int, количество лепестков.
    :param r: float, радиус лепестка.
    '''

    a = 360 / n

    for i in range(n):
        draw_circle(r)
        turtle.left(a)


def draw_butterfly(n: int = 10, s_r: float = 50, inc: float = 10):
    '''
    Упражнение 11.

    Рисует бабочку.

    :param n: int, число парных узоров.
    :param s_r: float, начальный радиус узора.
    :param inc: float, приращение радиуса узора.
    '''

    turtle.left(90)

    c_r = s_r

    for i in range(n):
        draw_circle(c_r)
        turtle.left(180)
        draw_circle(c_r)
        c_r += inc


def draw_curve(a: float = 180, r: float = 50):
    '''
    Упражнение 12.

    Рисует дугу

    :param a: float, угол дуги.
    :param r: float, радиус окружности.
    '''

    length = math.pi * r * a / 180

    for i in range(a):
        turtle.forward(length / a)
        turtle.left(1)


def draw_spring(n: int = 10, r1: int = 50, r2: int = 5):
    '''
    Упражнение 12.

    Рисует дугу.

    :param n: int, количество узлов.
    :param r1: float, радиус большой дуги.
    :param r2: float, радиус малой дуги
    '''

    for i in range(n):
        draw_curve(180, 50)
        draw_curve(180, 5)


def draw_smiley_face(r1: float = 100):
    '''
    Упражнение 13.

    Рисует смайлик.
    '''

    turtle.begin_fill()
    draw_circle(r1)
    turtle.color('#FFFF00')
    turtle.end_fill()
    turtle.color('#000000')

    r2 = r1 * 0.15

    for i in range(2):

        turtle.penup()
        eye_position = [r1 * (0.5 if i ==0 else -0.5), r1 * 2 * 0.65]
        turtle.goto(eye_position[0],eye_position[1])
        turtle.pendown()

        turtle.begin_fill()
        draw_circle(r2)
        turtle.color('#0000FF')
        turtle.end_fill()

        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        turtle.color('#000000')


    nose_length = r1 * 2 * 0.2
    nose_width = r1 * 0.1
    nose_position = [0,r1 * 2 * 0.65]

    turtle.penup()
    turtle.goto(nose_position[0], nose_position[1])
    turtle.pendown()

    turtle.left(90)
    turtle.width(nose_width)
    turtle.backward(nose_length)
    turtle.right(90)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    mouth_position = [r1*-0.4,r1*0.45]
    mouth_width = r1 * 0.1

    turtle.penup()
    turtle.goto(mouth_position[0], mouth_position[1])
    turtle.pendown()
    turtle.color('#FF0007')
    turtle.width(mouth_width)

    turtle.right(60)
    draw_curve(120, r1*0.5)


def draw_star(n:int = 11, l:float = 200):
    '''
    Упражнение 14.

    Рисует звезду.

    :param n: int, количество концов звезды.
    :param l: float, длина луча.
    '''


    if n % 2 == 0:
        raise IOError("У звезды должно быть нечетное количество лучей.")

    a = 360 / n * (n // 2)

    turtle.left(a)

    for i in range(n):
        turtle.left(a)
        turtle.forward(l)


draw_regular_polygons(40, 40, 10)


m_turtle.done()

