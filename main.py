from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

in_game = True


def snake_game():

    while in_game:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            scoreboard.update_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset_score()
            snake.reset_position()

        # Detect collision with tail
        for part in snake.snake_body[1:]:
            if snake.head.distance(part) < 10:
                scoreboard.reset_score()
                snake.reset_position()


    screen.exitonclick()


snake_game()
