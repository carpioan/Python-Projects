import turtle

#create a triangle.
def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("white")

    eve = turtle.Turtle()
    eve.shape("classic")
    eve.color("red")
    eve.begin_fill()
    eve.speed(3)
    eve.forward(20)
    eve.left(120)
    eve.forward(20)
    eve.left(120)
    eve.forward(20)
    eve.forward(20)
    eve.left(120)
    eve.forward(20)
    eve.left(120)
    eve.forward(20)
    eve.up()
    eve.right(120)
    eve.forward(20)
    eve.down()
    eve.right(120)
    eve.forward(20)
    eve.left(120)
    eve.forward(20)
    eve.left(120)
    eve.forward(20)
    eve.end_fill()

    window.exitonclick()

draw_triangle()