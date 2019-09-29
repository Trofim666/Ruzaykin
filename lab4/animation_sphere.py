import graphics as gr

from math import sin
from math import cos
from math import pi
from math import sqrt

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


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)

    return new_point


def ball_go(position):
    ball.move(speed.x, speed.y)
    position = add(position, speed)


def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
    
    return scalar


def change_speed(velocity, x, y):
    pass


def vector_along_radius(x,y):
    length_vector = sqrt( (x_0 - x)**2 + (y_0 - y)**2 )
    vector_along_r = gr.Point( (x_0 - x)/length_vector , (y_0 - y)/length_vector )
    
    return vector_along_r


def vector_normal_radius(x,y):
    length_vector = sqrt( (x_0 - x)**2 + (y_0 - y)**2 )
    vector_normal_r = gr.Point( (y_0 - y)/length_vector , -(x_0 - x)/length_vector )
    
    return vector_normal_r
    

def check_position():
    pass
        


while True:
    ball_go(position)
    
    x = position.x
    y = position.y
    
    
    gr.time.sleep(0.02)
