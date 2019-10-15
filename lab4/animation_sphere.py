import graphics as gr

from math import sqrt
                                                                               
SIZE_X = 1000
SIZE_Y = 650

position1 = gr.Point(600,310)
position2 = gr.Point(400,210)
speed1 = gr.Point(20,3)
speed2 = gr.Point(9,9)

x_0 = 500
y_0 = 325


window = gr.GraphWin("OknO", SIZE_X, SIZE_Y)
window.setBackground('aqua')


def draw_mouth():
    my_rectangle = gr.Rectangle(gr.Point(350, 450), gr.Point(660, 500))
    my_rectangle.setWidth(1)
    my_rectangle.draw(window)
    my_rectangle.setFill('blue')

    
def draw_eye1():
    eye_1 = gr.Circle(gr.Point(630, 175), 40)
    eye_1.setFill('white')
    eye_1.setOutline('black')
    eye_1.setWidth(10)
    eye_1.draw(window)
    

def draw_eye2():
    eye_1 = gr.Circle(gr.Point(470, 175), 40)
    eye_1.setFill('white')
    eye_1.setOutline('black')
    eye_1.setWidth(10)
    eye_1.draw(window)


def draw_big_circle():
    my_big_circle = gr.Circle(gr.Point(x_0, y_0), 300)
    my_big_circle.draw(window)
    my_big_circle.setFill('green')
    my_big_circle.setOutline('yellow')
    my_big_circle.setWidth(20)
    

def draw_ball(position, i):
    color = ['red', 'yellow', 'green', 'black', 'aqua']
    ball = gr.Circle(position, 30)
    ball.draw(window)
    ball.setFill(color[i])
    return ball


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)

    return new_point


def ball_go(ball, speed):
    ball.move(speed.x, speed.y)


def scalar_x_vector(scalar, vector):
    new_vector = gr.Point(scalar*vector.x, scalar*vector.y)
    
    return new_vector


def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x*vector_2.x + vector_1.y*vector_2.y
    
    return scalar


def changed_speed(speed, x, y):
    speed_along_r = scalar_x_vector(
        scalar_multiplication(
            vector_along_radius(x, y),
            speed
        ),
        vector_along_radius(x,y)
    )
    
    speed_normal_r = scalar_x_vector(
        scalar_multiplication(
            vector_normal_radius(x, y),
            speed
        ),
        vector_normal_radius(x, y)
    )
    
    speed_along_r_new = scalar_x_vector(-1, speed_along_r)
    
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


def vector_along_radius(x, y):
    length_vector = sqrt((x_0-x)**2 + (y_0-y)**2)
    vector_along_r = gr.Point(
        (x_0-x) / length_vector,
        (y_0-y) / length_vector
    )
    
    return vector_along_r


def vector_normal_radius(x,y):
    length_vector = sqrt((x_0 - x)**2 + (y_0 - y)**2 )
    vector_normal_r = gr.Point((y_0-y)/length_vector, - (x_0-x)/length_vector)
    
    return vector_normal_r
    

def check_position(speed, x, y):
    if (x_0-x)**2 + (y_0-y)**2 >= 260**2:
        speed = changed_speed(speed, x, y)
        
    return speed
        

draw_big_circle()

draw_eye1()
draw_eye2()
draw_mouth()

ball1 = draw_ball(gr.Point(600,310), 0)
ball2 = draw_ball(gr.Point(400,210), 4)

while True:
    ball_go(ball1, speed1)
    ball_go(ball2, speed2)
    
    position1 = add(position1, speed1)
    position2 = add(position2, speed2)
    
    x1 = position1.x
    y1 = position1.y
    
    x2 = position2.x
    y2 = position2.y
    
    if (x2-x1)**2 + (y2-y1)**2 <= 15**2:
        speed1 = gr.Point(-speed2.y*8/9, speed2.x*7/8)
        speed2 = gr.Point(speed1.y*9/10, -speed1.x*8/11)
    
    speed1 = check_position(speed1, x1, y1)
    speed2 = check_position(speed2, x2, y2)
    
    speed1 = gr.Point(speed1.x*1.001, speed1.y*1.001)
    speed2 = gr.Point(speed2.x*1.001, speed2.y*1.001)
    
    gr.time.sleep(0.02)
