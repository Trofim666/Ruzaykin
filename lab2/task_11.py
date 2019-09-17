import turtle as t

t.shape("turtle")
t.right(90)
k=0
for k in range(8):
	k+=1
	for i in range(100):
		t.forward(2+k)
		t.left(360/100)
	for i in range(100):
		t.forward(2+k)
		t.right(360/100)
	
input()
