# import the required librabries and functions
import time
from turtle import Screen
from ball import Ball
from bat import Paddle
from scoreboard import ScoreBoard
from wall import Blocks

# screen setup
screen = Screen()
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

# objects
bouncing_ball = Ball()
player = Paddle((0, -250))
blocks = Blocks()
score_and_turn = ScoreBoard()

# set screen listen
screen.listen()
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")


def restart():
    """takes no arguments. starts game when called"""

    bounce_count = 0
    # condition for running the game
    game_on = True
    while game_on:

        screen.update()
        # move ball around
        time.sleep(bouncing_ball.gamespeed)
        bouncing_ball.move_around()
        x = bouncing_ball.xcor()
        y = bouncing_ball.ycor()
        score_and_turn.update_score()

        # game over
        if score_and_turn.lives == 0:
            score_and_turn.game_over()
            game_on = False


        # detect collision with top wall
        if y > 330:
            bouncing_ball.bounce_wall()

        # miss
        if bouncing_ball.ycor() < -330:
            bouncing_ball.reset_position()
            bounce_count = 0
            player.shapesize(stretch_len=2)
            score_and_turn.lives -= 1
            score_and_turn.clear()
            score_and_turn.update_score()

        # collision with left and right wall
        if x > 280 or x < -280:
            bouncing_ball.bounce_up()

        # detect successful hit
        if bouncing_ball.distance(player) < 40 and bouncing_ball.ycor() < -230:
            bouncing_ball.bounce_wall()
            bounce_count += 1

        # collision with the different coloured bricks
        for i in range(len(blocks.yellow_list)):
            if blocks.yellow_list[i].distance(bouncing_ball) < 20:
                blocks.disappear(blocks.yellow_list[i])
                bouncing_ball.bounce_wall()
                score_and_turn.score += 1
                score_and_turn.clear()
                score_and_turn.update_score()

            if blocks.green_list[i].distance(bouncing_ball) < 20:
                blocks.disappear(blocks.green_list[i])
                bouncing_ball.bounce_wall()
                score_and_turn.score += 3
                score_and_turn.clear()
                score_and_turn.update_score()

            if blocks.orange_list[i].distance(bouncing_ball) < 20:
                blocks.disappear(blocks.orange_list[i])
                bouncing_ball.bounce_wall()
                bouncing_ball.change_speed()
                score_and_turn.score += 5
                score_and_turn.clear()
                score_and_turn.update_score()

            if blocks.red_list[i].distance(bouncing_ball) < 20:
                blocks.disappear(blocks.red_list[i])
                bouncing_ball.bounce_wall()
                bouncing_ball.change_speed()
                player.shapesize(stretch_len=1)
                score_and_turn.score += 7
                score_and_turn.clear()
                score_and_turn.update_score()

        # increase speed
        if bounce_count % 4 == 0 and bounce_count > 0:
            bouncing_ball.change_speed()
            print(bounce_count)





restart()

screen.exitonclick()