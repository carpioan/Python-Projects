import turtle

def first_letter():
    window = turtle.Screen()
    window.bgcolor("white")

    i = turtle.Turtle()
    i.setheading(90)
    i.forward(100)
    i.shape("classic")
    i.color("purple")
    i.speed(10)

    window.exitonclick()

def second_letter():
    o = turtle.Turtle()
    o.shape("classic")
    o.color("purple")
    o.speed(10)
    o.penup()
    o.setx(30)
    #o.setheading(360)
    o.pendown()
    for item in range(1, 3):
        o.forward(50)
        o.right(90)
        o.forward(100)
        o.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    first_letter()
    second_letter()

    window.exitonclick()

draw_art()