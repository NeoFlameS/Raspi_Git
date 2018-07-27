from turtle import *
speed(0)
bgcolor('black')
pencolor('white')
x=0
up();rt(45);fd(50);rt(135);down()
colors=['red','purple','blue','orange','yellow','white']
while x<120:
	for i in range(6):
		fd(100);rt(62);pencolor(colors[i])
	lt(50)
	x=x+1
exitonclick()