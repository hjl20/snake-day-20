from turtle import Turtle

COLOR = "white"
SCREEN_HEIGHT = 250
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.goto(0, SCREEN_HEIGHT)
        self.score = 0
        self.show_score()
        self.hideturtle()

    def show_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
