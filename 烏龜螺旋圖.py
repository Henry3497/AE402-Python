import turtle
jack = turtle.Turtle()
jack.shape("turtle")
jack.penup()
for i in range(0, 100 ,5):
    jack.forward(30+i)
    jack.right(30)
    jack.stamp()
