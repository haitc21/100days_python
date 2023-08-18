from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_socreboard()

    def update_socreboard(self):
        self.write(f"Điểm: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_socreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"TOANG...", align=ALIGNMENT, font=FONT)

