import graphics as gr

from math import sin
from math import cos
from math import pi
from math import acos

SIZE_X = 1000
SIZE_Y = 650

window = gr.GraphWin("OknO", SIZE_X, SIZE_Y)
window.setBackground('aqua')

position = gr.Point(500,325)
speed = gr.Point(3,3)

x_0 = 500
y_0 = 325

my_big_circle = gr.Circle(gr.Point(x_0, y_0), 300)
my_big_circle.draw(window)
my_big_circle.setFill('yellow')
my_big_circle.setOutline('green')
my_big_circle.setWidth(20)

ball = gr.Circle(position, 10)
ball.draw(window)
ball.setFill('red')

def go():
    pass


def scalar_multiplication():
    pass


def change_speed():
    pass


def check_position():
    pass


while True:
    ball.move(speed.x,speed.y)

    
    gr.time.sleep(0.02)
