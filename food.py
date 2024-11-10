from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("gold")
        self.speed("fastest")
        self.regenerate()


    def regenerate(self):
        random_x = random.randint(-180, 180)
        random_y = random.randint(-180, 180)
        self.goto(random_x, random_y)
        print(f'{self.pos()}')