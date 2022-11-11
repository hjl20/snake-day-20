from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = "square"
COLOR = "white"


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle(SHAPE)
        snake_part.color(COLOR)
        snake_part.penup()
        snake_part.goto(position)
        self.snake_body.append(snake_part)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for part in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[part].goto(self.snake_body[part - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_position(self):
        for part in self.snake_body:
            part.goto(1000, 1000)
        self.__init__()

