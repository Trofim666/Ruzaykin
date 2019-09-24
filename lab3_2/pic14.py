import graphics as gr
window = gr.GraphWin("Dog", 600, 800)


def draw_back1(w):
    
    my_rectangle_1 = gr.Rectangle(gr.Point(0, 0), gr.Point(600,500 ))
    my_rectangle_1.draw(window)
    my_rectangle_1.setFill('blue')

def draw_back2(w):
    
    my_rectangle_2 = gr.Rectangle(gr.Point(0, 500), gr.Point(600,800))
    my_rectangle_2.draw(window)
    my_rectangle_2.setFill('green')
    my_line = gr.Line(gr.Point(0, 500), gr.Point(600, 500))

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