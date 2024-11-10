from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = -1
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f'GAME OVER n Score: {self.score}', align="center", font=("Arial", 10, "normal"))