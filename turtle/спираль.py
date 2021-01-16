from turtle import*

speed(5)
width(5)
color('pink')
length = 10
count = 0
while count < 30 :
    forward(length)
    left(120)
    length = length + 10
    count =count + 1
exitonclick()
