from turtle import Screen, Turtle, write
import snake
import time
from food import Food
from score import Score

screen = Screen()
print(screen.getshapes())
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake game")
screen.tracer(0)

snake = snake.Snake()
food_unit = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if not snake.check_edges():
        game_over = True
        score.game_is_over()

    if snake.head.distance(food_unit) < 15:
        food_unit.refresh()
        score.add_score()
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_over = True
            score.game_is_over()

screen.exitonclick()
