import graphics as gr

from math import sin
from math import cos
from math import pi

SIZE_X = 1000
SIZE_Y = 650

window = gr.GraphWin("OknO", SIZE_X, SIZE_Y)
window.setBackground('aqua')

my_circle = gr.Circle(gr.Point(500, 325), 300)
my_circle.draw(window)
my_circle.setFill('yellow')
my_circle.setOutline('green')
my_circle.setWidth(20)

window.getMouse()
window.close()