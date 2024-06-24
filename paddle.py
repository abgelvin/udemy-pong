from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5, 1)
        if position == 'left':
            self.goto(-350, 0)
        elif position == 'right':
            self.goto(350, 0)


    def move_up(self):
        new_y = self.ycor() + 20
        if new_y > 250:
            pass
        else:
             self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        if new_y < -250:
            pass
        else:
            self.goto(self.xcor(), new_y)