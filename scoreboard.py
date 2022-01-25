from turtle import Turtle
X_POSITION = 0
Y_POSITION = 270
ALIGNMENT = "center"
FONT = ('Arial', 20, "bold")
with open("data.txt") as file:
    high_score = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.high_score = high_score
        self.penup()
        self.pencolor("white")
        self.goto(X_POSITION, Y_POSITION)
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0

        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
