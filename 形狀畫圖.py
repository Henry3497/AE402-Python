import turtle
jack = turtle.Turtle()
a = input("你想畫幾邊形?")
a = int(a)
for i in range(a):
    jack.forward(100)
    jack.left(360/a)

