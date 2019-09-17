import graphics as gr

window = gr.GraphWin("PeyZaj", 400, 400)

Pr_1 = gr.Rectangle(gr.Point(0,0), gr.Point(400,150))
Pr_1.setFill("green")
Pr_1.draw(window)

Pr_2 = gr.Rectangle(gr.Point(0,150), gr.Point(400,400))
Pr_2.setFill("red")
Pr_2.draw(window)

my_circle = gr.Circle(gr.Point(200, 200), 100)
my_circle.setFill("purple")
my_circle.draw(window)

Pr_3 = gr.Rectangle(gr.Point(130,240), gr.Point(270,260))
Pr_3.setFill("blue")
Pr_3.draw(window)

my_circl = gr.Circle(gr.Point(200, 200), 40)
my_circl.setFill("yellow")
my_circl.draw(window)

glaz1 = gr.Polygon(gr.Point(150,120),gr.Point(120,150),gr.Point(180,150))
glaz1.setFill("black")
glaz1.draw(window)

glaz1 = gr.Polygon(gr.Point(250,120),gr.Point(220,150),gr.Point(280,150))
glaz1.setFill("black")
glaz1.draw(window)

my_circle1 = gr.Circle(gr.Point(200, 200), 15)
my_circle1.setFill("orange")
my_circle1.draw(window)

my_circle2 = gr.Circle(gr.Point(150, 140), 10)
my_circle2.setFill("yellow")
my_circle2.draw(window)

my_circle3 = gr.Circle(gr.Point(250, 140), 10)
my_circle3.setFill("yellow")
my_circle3.draw(window)

my_circle4 = gr.Circle(gr.Point(150, 140), 4)
my_circle4.setFill("red")
my_circle4.draw(window)

my_circle5 = gr.Circle(gr.Point(250, 140), 4)
my_circle5.setFill("red")
my_circle5.draw(window)



window.getMouse()
window.close()


