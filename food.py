from turtle import Turtle
import random

colors = [
    "red",
    "yellow",
    "blue",
    "orange",
    "purple",
    "pink",
    "white",
    "cyan",
    "magenta",
    "black"
]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.8)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        random_color = random.choice(colors)
        self.color(random_color)
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x_random, y_random)
