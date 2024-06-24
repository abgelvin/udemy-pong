from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
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

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision with paddle
    if ball.xcor() > 280 and ball.distance(r_paddle) < 30 or ball.xcor() < -280 and ball.distance(l_paddle) < 30:
        ball.hit()

    #Detect missed ball
    if ball.xcor() > 300:
        

    
screen.exitonclick()