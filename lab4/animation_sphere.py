import graphics as gr

from math import sqrt

SIZE_X = 1000
SIZE_Y = 650

window = gr.GraphWin("OknO", SIZE_X, SIZE_Y)
window.setBackground('aqua')

position = gr.Point(600,310)
speed = gr.Point(3,7)

x_0 = 500
y_0 = 325

my_big_circle = gr.Circle(gr.Point(x_0, y_0), 300)
my_big_circle.draw(window)
my_big_circle.setFill('yellow')
my_big_circle.setOutline('green')
my_big_circle.setWidth(20)

ball = gr.Circle(position, 30)
ball.draw(window)
ball.setFill('red')


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)

    return new_point


def ball_go():
    ball.move(speed.x, speed.y)


def scalar_x_vector(scalar,vector):
    new_vector = gr.Point( scalar*vector.x, scalar*vector.y )
    
    return new_vector


def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
    
    return scalar


def changed_speed(speed, x, y):
    speed_along_r = scalar_x_vector (scalar_multiplication (vector_along_radius(x,y), speed),
                                    vector_along_radius(x,y))
    
    speed_normal_r = scalar_x_vector (scalar_multiplication (vector_normal_radius(x,y), speed),
                                     vector_normal_radius(x,y))
    
    speed_along_r_new = scalar_x_vector (-1, speed_along_r)
    
    i = gr.Point(1, 0)
    j = gr.Point(0, 1)
    
    speed_projection_1_x = scalar_multiplication (speed_along_r_new, i)
    speed_projection_2_x = scalar_multiplication (speed_normal_r, i)
    
    speed_projection_1_y = scalar_multiplication (speed_along_r_new, j)
    speed_projection_2_y = scalar_multiplication (speed_normal_r, j)
    
    speed_x = speed_projection_1_x + speed_projection_2_x
    speed_y = speed_projection_1_y + speed_projection_2_y
    
    speed = gr.Point(speed_x, speed_y)
    return speed

def vector_along_radius(x,y):
    length_vector = sqrt( (x_0 - x)**2 + (y_0 - y)**2 )
    vector_along_r = gr.Point( (x_0 - x)/length_vector , (y_0 - y)/length_vector )
    
    return vector_along_r


def vector_normal_radius(x,y):
    length_vector = sqrt( (x_0 - x)**2 + (y_0 - y)**2 )
    vector_normal_r = gr.Point( (y_0 - y)/length_vector , -(x_0 - x)/length_vector )
    
    return vector_normal_r
    

def check_position(speed, x, y):
    if (x_0 - x)**2 + (y_0 - y)**2 >= 260**2:
        speed = changed_speed(speed, x, y)
        
    return speed
        
    
while True:
    ball_go()

    position = add(position, speed) 
    
    x = position.x
    y = position.y
    
    #Абсолютно неясно, почему не работает прога, ежели я вместо строки ниже напишу что-нибудь like this: 
    # check_position(speed, x, y)  !!! при условии, что в функции не будет return. That is the question...
    
    speed = check_position(speed, x, y)
     
    
    gr.time.sleep(0.02)
