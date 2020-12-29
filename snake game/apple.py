import random
from snake import Snake
from snake import field
s = Snake()
class Apple:
    def __init__(self):
        self.x = random.randint(-1, field)
        self.y = random.randint(-1, field)
        self.score = 0


    def eaten(self):
        self.x = random.randint(-1, field)
        self.y = random.randint(-1, field)
        self.score += 1
        s.snake_length += 1

