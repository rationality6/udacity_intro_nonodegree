import turtle


class InnerTurtle(turtle.Turtle):
    """
    inheritance
    """
    default_shape = 'turtle'
    default_color = 'black'
    default_speed = 4
    print("Inheritance call")

    def set_infos(self, shape=default_shape, color=default_color, speed=default_speed):
        self.shape(shape)
        self.color(color)
        self.speed(speed)

    def draw_lines(self, lines, size, turn):
        for i in range(0, lines):
            self.forward(size)
            self.right(turn)

    def draw_circle(self, size):
        self.circle(size)

window = turtle.Screen()
window.bgcolor("blue")

brad = InnerTurtle()
brad.set_infos('turtle', 'red', 4)
brad.draw_lines(4, 100, 90)

angie = InnerTurtle()
angie.set_infos('arrow', 'yellow', 10)
angie.draw_circle(150)

google = InnerTurtle()
google.set_infos()
google.draw_lines(3, 170, 120)

window.exitonclick()
