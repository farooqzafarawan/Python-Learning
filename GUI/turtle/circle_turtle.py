import turtle

t = turtle.Turtle()

rad = 10
num = 5

for i in range(1, num+1):
    t.circle(rad*i)

turtle.done()