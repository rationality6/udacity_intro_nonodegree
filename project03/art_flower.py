import turtle

window = turtle.Screen()
window.bgcolor("blue")


def set_brad():
    brad = turtle.Turtle("turtle")
    brad.shape("turtle")
    brad.color("red")
    brad.speed(56)
    return brad


def draw_square(who):
    while(True):
        for i in range(0, 4):
            who.forward(100)
            who.right(90)
        who.right(2)

draw_square(set_brad())

window.exitonclick()
