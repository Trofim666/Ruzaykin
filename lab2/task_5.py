import turtle as t

for i in range(10):
	for k in range(4):
		t.forward((i+10)*20)
		t.left(90)
	t.penup()
	t.right(180)
	t.forward(10)
	t.left(90)
	t.forward(10)
	t.pendown()
	t.left(90)
input()
