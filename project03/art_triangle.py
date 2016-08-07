import turtle

window = turtle.Screen()
window.bgcolor("blue")


def set_brad():
    brad = turtle.Turtle("turtle")
    brad.shape("turtle")
    brad.color("red")
    brad.speed(16)
    return brad


def draw_square(who):
    who.right(120)
    for i in range(0, 3):
        who.forward(300)
        who.left(120)
    while(True):


draw_square(set_brad())

window.exitonclick()
