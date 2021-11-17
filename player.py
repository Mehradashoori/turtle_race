from turtle import Turtle

import car_manager
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def restart_position(self):
        self.goto(STARTING_POSITION)


