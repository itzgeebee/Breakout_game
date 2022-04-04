from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 000
        self.lives = 4
        self.color("white")
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        """ updates the score board"""
        self.goto(-260, 240)
        self.write(arg=self.score, move=False, align='left', font=('Courier', 60, 'normal'))
        self.goto(130, 240)
        self.write(arg=f"00{self.lives}", move=False, align='left', font=('Courier', 60, 'normal'))

    def game_over(self):
        """prints out the final messages when game termination condition is met"""
        self.goto(-150, 0)
        self.write(arg="Game Over", move=False, align='left', font=('Courier', 50, 'normal'))
