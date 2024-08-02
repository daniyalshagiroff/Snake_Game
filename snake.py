from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in positions:
            self.add_seg(position)

    def add_seg(self, position):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("yellow")
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for t_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[t_num - 1].xcor()
            y = self.segments[t_num - 1].ycor()
            self.segments[t_num].goto(x, y)
        self.head.forward(move_distance)

    def left(self):
        if self.head.heading() == EAST:
            return
        self.head.setheading(WEST)

    def right(self):
        if self.head.heading() == WEST:
            return
        self.head.setheading(EAST)

    def up(self):
        if self.head.heading() == SOUTH:
            return
        self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() == NORTH:
            return
        self.head.setheading(SOUTH)

    def check_edges(self):
        if self.head.xcor() > 300:
            return False
        elif self.head.ycor() > 300:
            return False
        elif self.head.xcor() < -300:
            return False
        elif self.head.ycor() < -300:
            return False
        return True

