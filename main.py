from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle('left')
r_paddle = Paddle('right')

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.hit()
        

    #Detect missed ball
    if ball.xcor() > 380:
        print('Player 2 missed.')
        scoreboard.increase_l_score()
        ball.reset_position()


    if ball.xcor() < -380:
        print('Player 1 missed.')
        scoreboard.increase_r_score()
        ball.reset_position()


    
screen.exitonclick()