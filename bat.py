from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.color("blue")
        self.goto(position)

    def move_right(self):
        """moves the paddle in the east direction"""

        new_x = (self.xcor() + 40)
        self.goto(new_x, self.ycor())

    def move_left(self):
        """moves the paddle in the west direction"""
        new_x = (self.xcor() - 40)
        self.goto(new_x, self.ycor())
