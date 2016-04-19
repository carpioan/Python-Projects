import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(other_turtle):
    for i in range(1, 4):
        other_turtle.forward(200)
        other_turtle.right(120)

def draw_hexagon(sec_turtle):
    for i in range(1, 7):
        sec_turtle.forward(125)
        sec_turtle.right(60)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    #Create turtle eve. Draw a circle.
    eve = turtle.Turtle()
    eve.shape("classic")
    eve.color("red")
    eve.speed(10)
    for i in range(1,61):
        draw_triangle(eve)
        eve.left(6)
    #Create turtle john. Draw a square.
    john = turtle.Turtle()
    john.shape("classic")
    john.color("purple")
    john.speed(10)
    for i in range(1,41):
        draw_square(john)
        john.right(9)
    adam = turtle.Turtle()
    adam.shape("classic")
    adam.color("green")
    adam.speed(12)
    for i in range(1,37):
        draw_hexagon(adam)
        adam.left(10)

    window.exitonclick()

draw_art()
