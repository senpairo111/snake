import random
from Snake import Snake
from settings import FIELD

# Global Variables
snake = Snake()

# Apple Class
class Apple:
    def __init__(self):
        self.x = random.randint(-1, FIELD)
        self.y = random.randint(-1, FIELD)
        self.score = 0


    def eaten(self):
        self.x = random.randint(-1, FIELD)
        self.y = random.randint(-1, FIELD)
        self.score += 1
        self.snake.snake_length += 1