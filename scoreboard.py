from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.color("black")
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
