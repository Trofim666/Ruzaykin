import graphics as gr
window = gr.GraphWin("Dog", 600, 700)


def draw_back1(w):
    
    my_rectangle_1 = gr.Rectangle(gr.Point(0, 0), gr.Point(600,450 ))
    my_rectangle_1.draw(window)
    my_rectangle_1.setFill('blue')

def draw_back2(w):
    """docs for function"""
    my_rectangle_2 = gr.Rectangle(gr.Point(0, 450), gr.Point(600,800))
    my_rectangle_2.draw(window)
    my_rectangle_2.setFill('green')
    my_line = gr.Line(gr.Point(0, 450), gr.Point(600, 450))

def draw_fence(win):
    pass

def  draw_dog(win):
    pass

def draw_booth(win):
    pass

def draw_chain(win):
    pass



def main(win):
    draw_back1(win)
    draw_back2(win)
    draw_fence(win)
    draw_dog(win)
    draw_booth(win)
    draw_chain(win)

main(window)
window.getMouse()
window.close()