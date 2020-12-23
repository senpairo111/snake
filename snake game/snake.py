field = 17
class Snake:

    def __init__(self):
        self.x = 8
        self.y = 8
        self.snake_life = True

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1
