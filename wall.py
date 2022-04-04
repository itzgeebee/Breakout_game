from turtle import Turtle

NUM_OF_TURTLES = 25
class Blocks:

    def __init__(self):

        self.red_list = []
        self.orange_list = []
        self.green_list = []
        self.yellow_list = []
        self.make_turtle()

    def make_turtle(self):
        """ makes bricks and display the bricks at the specified positions"""
        n = -290
        for i in range(NUM_OF_TURTLES):
            red, orange, green, yellow = Turtle("square"), Turtle("square"), Turtle("square"), Turtle("square")
            red1, orange1, green1, yellow1 = Turtle("square"), Turtle("square"), Turtle("square"), Turtle("square")
            red.penup(), orange.penup(), green.penup(), yellow.penup()
            red1.penup(), orange1.penup(), green1.penup(), yellow1.penup()
            red.color("red"), orange.color("orange"), green.color("green"), yellow.color("yellow")
            red1.color("red"), orange1.color("orange"), green1.color("green"), yellow1.color("yellow")
            red.shapesize(stretch_len=1, stretch_wid=0.4), orange.shapesize(stretch_len=1, stretch_wid=0.4), \
            green.shapesize(stretch_len=1, stretch_wid=0.4), yellow.shapesize(stretch_len=1, stretch_wid=0.4),
            red1.shapesize(stretch_len=1, stretch_wid=0.4), orange1.shapesize(stretch_len=1, stretch_wid=0.4), \
            green1.shapesize(stretch_len=1, stretch_wid=0.4), yellow1.shapesize(stretch_len=1, stretch_wid=0.4),
            red.goto(n, 210),\
            orange.goto(n, 182),  green.goto(n, 154),  \
            yellow.goto(n, 126),
            red1.goto(n, 196), orange1.goto(n, 168), green1.goto(n, 140), yellow1.goto(n, 112)
            n += 24
            self.red_list.append(red)
            self.red_list.append(red1)
            self.orange_list.append(orange)
            self.orange_list.append(orange1)
            self.green_list.append(green)
            self.green_list.append(green1)
            self.yellow_list.append(yellow)
            self.yellow_list.append(yellow1)


    def disappear(self, block):
        """relocates bricks off screen"""
        block.goto(-2000, 2000)






