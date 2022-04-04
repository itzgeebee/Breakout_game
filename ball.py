
# The ball class which defines the attributes and methods of the ball
import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.2, stretch_len=0.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.gamespeed = 0.1

    def move_around(self):
        """moves ball from the initial coordinate to the right side """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        """changes y coordinates of the  ball direction """
        self.y_move *= -1

    def bounce_up(self):
        """changes x coordinates of the  ball direction """
        self.x_move *= -1

    def reset_position(self):
        """returns the ball to the starting position"""
        self.goto(0, -200)
        self.gamespeed = 0.1
        time.sleep(3)
        self.bounce_wall()

    def change_speed(self):
        """changes ball speed"""
        self.gamespeed *= 0.95
