from turtle import *
shape("turtle")
for i in range(100):
	if i%2==0:
		forward(i*2)
		left(100)
	else:
		forward(i)
		right(20)