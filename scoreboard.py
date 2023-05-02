from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Cambria", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as high_score:
            self.high_score = high_score.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as new_high_score:
                new_high_score.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
