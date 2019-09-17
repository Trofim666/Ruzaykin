import turtle as t

t.shape("turtle")
for i in range(3):
	for i in range(100):
		t.forward(5)
		t.left(360/100)
	for i in range(100):
		t.forward(5)
		t.right(360/100)
		
	t.left(60)


input()

