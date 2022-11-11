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
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.show_score()
        self.hideturtle()

    def show_score(self):
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.show_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
