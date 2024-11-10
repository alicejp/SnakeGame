from turtle import Screen, Turtle

UP = 90.0
DOWN = 270.0
LEFT = 180.0
RIGHT = 0.0


class Snake:

    def __init__(self, snake_len, name, age):
        self.snake_len = snake_len
        self.name = name
        self.age = age
        self.snake_body = []
        self.snake_pos = []
        self.snake_heading = []
        self.to_heading = 0

        # create snake
        for index in range(snake_len):
            self.add_body((-20 * index, 0))

    def add_body(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.snake_body.append(t)
        self.snake_heading.append(t.heading())
        self.snake_pos.append(t.pos())
        print(f'add_body position: {position}')

    def extend(self):
        # for bd in self.snake_body:
        #     print(f'extend, snake_body: {bd.position()}')

        # snake_body[-1] is the last one
        if self.snake_body[-1].heading() == UP:
            next_body_pos = (0, -20)
        elif self.snake_body[-1].heading() == DOWN:
            next_body_pos = (0, 20)
        elif self.snake_body[-1].heading() == RIGHT:
            next_body_pos = (-20, 0)
        else:
            next_body_pos = (20, 0)
        # print(f'extend, position: {self.snake_body[-1].position() + next_body_pos}')
        self.add_body(self.snake_body[-1].position() + next_body_pos)

    def move(self):
        for index in range(len(self.snake_body)):
            if index == 0:
                self.snake_body[index].setheading(self.to_heading)
            else:
                self.snake_body[index].setheading(self.snake_heading[index - 1])

            self.snake_body[index].forward(20)

        for index in range(len(self.snake_body)):
            self.snake_heading[index] = self.snake_body[index].heading()

    def up(self):
        if self.snake_heading[0] == UP:
            # print(f'cannot go UP, because it is facing UP')
            return
        elif self.snake_heading[0] != DOWN:
            print(f'UP self.to_heading: {self.snake_heading[0]}')
            self.to_heading = UP
        else:
            print(f'cannot go UP, because it is facing DOWN')

    def down(self):
        if self.snake_heading[0] == DOWN:
            # print(f'cannot go DOWN, because it is facing DOWN')
            return
        elif self.snake_heading[0] != UP:
            print(f'DOWN self.to_heading: {self.snake_heading[0]}')
            self.to_heading = DOWN
        else:
            print(f'cannot go DOWN, because it is facing UP')

    def left(self):
        if self.snake_heading[0] == LEFT:
            # print(f'cannot go LEFT, because it is facing LEFT')
            return

        elif self.snake_heading[0] != RIGHT:
            print(f'LEFT self.to_heading: {self.snake_heading[0]}')
            self.to_heading = LEFT
        else:
            print(f'cannot go LEFT, because it is facing RIGHT')

    def right(self):
        if self.snake_heading[0] == RIGHT:
            # print(f'cannot go RIGHT, because it is facing RIGHT')
            return
        elif self.snake_heading[0] != LEFT:
            print(f'RIGHT self.to_heading: {self.snake_heading[0]}')
            self.to_heading = RIGHT
        else:
            print(f'cannot go RIGHT, because it is facing LEFT')
