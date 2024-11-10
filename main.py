# This is a sample Python script.
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

X_MAX = 250
X_MIN = -250
Y_MAX = 250
Y_MIN = -250

screen = Screen()
# -280, 280 as the wall
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My awesome game")
screen.tracer(0)

sn = Snake(5, "J", 10)
fd = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(sn.up, "w")
screen.onkey(sn.down, "s")
screen.onkey(sn.left, "a")
screen.onkey(sn.right, "d")

print(f'snake_heading before{sn.snake_heading}')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # one sec delay
    sn.move()

    # yum yum
    if sn.snake_body[0].distance(fd) < 15:
        fd.regenerate()
        sb.update_score()
        sn.extend()

    # Collide to the wall
    if sn.snake_body[0].xcor() > X_MAX or sn.snake_body[0].xcor() < X_MIN or sn.snake_body[0].ycor() > Y_MAX or sn.snake_body[0].ycor() < Y_MIN:

        # CounterClockwise
        if sn.snake_body[0].xcor() > X_MAX:
            sn.up()
            if sn.snake_body[0].ycor() > Y_MAX:
                sn.left()
        elif sn.snake_body[0].xcor() < X_MIN:
            sn.down()
            if sn.snake_body[0].ycor() < Y_MIN:
                sn.right()
        elif sn.snake_body[0].ycor() > Y_MAX:
            sn.left()
        elif sn.snake_body[0].ycor() < Y_MIN:
            sn.right()
        # game_is_on = False
        # sb.game_over()

    # Collide into its own body
    # Or write like this sn.snake_body[1:]
    for body in sn.snake_body:
        if body == sn.snake_body[0]:
            pass
        elif sn.snake_body[0].distance(body) < 10:
            body.color("gold")

print(f'snack heading after {sn.snake_heading}')


screen.exitonclick()
