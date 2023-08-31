from turtle import Turtle
MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)
        self.color("white")

    def move_up(self):
        if self.ycor() > 230:
            pass
        else:
            new_y = self.ycor() + MOVEMENT
            current_x = self.xcor()
            self.goto(current_x, new_y)

    def move_down(self):
        if self.ycor() < -220:
            pass
        else:
            new_y = self.ycor() - MOVEMENT
            current_x = self.xcor()
            self.goto(current_x, new_y)
