import random
from snake import Snake
s = Snake()
from snake import field
class Apple:
    def __init__(self):
        self.x = random.randint(0, field)
        self.y = random.randint(0, field)
        self.score = 0


    def eaten(self):
        self.x = random.randint(0, field)
        self.y = random.randint(0, field)
        self.score += 1
