from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "blue"
SPEED = "fastest"
STRETCH_LEN = 0.5
STRETCH_WID = 0.5
SCREEN_WIDTH = 280
SCREEN_HEIGHT = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)
        self.color(COLOR)
        self.speed(SPEED)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
        rand_y = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
        self.goto(rand_x, rand_y)
