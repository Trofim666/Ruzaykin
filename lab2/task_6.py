import turtle as t 

n=int(input())
t.shape("turtle")
for i in range(n):
	t.forward(200)
	t.stamp()
	t.right(180)
	t.forward(200)
	t.right(180)
	t.left(360/n)
input()

	
	
