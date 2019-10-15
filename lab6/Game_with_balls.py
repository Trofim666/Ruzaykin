from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')


score = 0

l = Label(root, bg='green', fg='yellow', width=50)
l.pack()

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue', 'purple']


balls = []

def new_ball():
    global x, y, r, i
    i +=1
    x = rnd(100, 700)
    y = rnd(100, 500)
    v_x = rnd(-10, 10)
    v_y = rnd(-10, 10)
    r = rnd(30, 50)
    id_ = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    ball = {'id' : id_, 'x': x, 'y': y, 'r' : r, 'v_x': v_x, 'v_y': v_y }
    balls.append(ball)
    root.after(1000 - i*1,new_ball)
    

def move_to():
    i = 0
    for b in balls:
        if (b['x'] > 800 - b['r']) or (b['x'] < b['r']):
            b['v_x'] = -b['v_x']*1.106
        if (b['y'] > 600 - b['r']) or (b['y'] < b['r']):
            b['v_y'] =  -b['v_y']*1.104
        canv.move(b['id'], b['v_x'], b['v_y'])
        b['y']+=b['v_y']
        b['x']+=b['v_x']
    root.after(40, move_to)


def click(event):
    global score
    
    for k,b in enumerate(balls):   
        if (event.x-b['x'])**2 + (event.y-b['y'])**2 <= b['r']**2:
            canv.delete(b['id'])
            del balls[k]
            score += 1
            j = 1
            l['text'] = 'Score:' + str(score)

        
new_ball()
move_to()
canv.bind('<Button-1>', click)
mainloop()