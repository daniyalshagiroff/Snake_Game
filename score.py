from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.color('white')
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"Score: {self.num}", False, "center", font=('Arial', 20, 'normal'))
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.num}", False, "center", font=('Arial', 20, 'normal'))

    def add_score(self):
        self.num += 1
        self.clear()
        self.update_score()

    def game_is_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write("Game Over :-(", False, "center", font=('Arial', 40, 'normal'))

