import turtle as t
from math import sin
from math import tan
from math import pi

a = 30

def storona(R):
	storona = R*2*tan(pi/n)
	return storona


t.shape("turtle")

def Radius(n):
	Radius =(a/(2*sin(pi/n)))
	return Radius


for i in range(10):
	n = i+3
	alfa_storon = (180 - 360/n)
	R = Radius(n)
	t.left(180 - alfa_storon/2)
	for k in range(n):
		t.forward(a)
		t.left(180-alfa_storon)
	R = R
	a = storona(R)
	
	t.left(180+alfa_storon/2)
	t.penup()
	t.forward(26)
	t.pendown()

input()
	
