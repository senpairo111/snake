import random
from Snake import Snake
from settings import FIELD

# Global Variables
snake = Snake()


# Apple Class
class Apple:
    def __init__(self):
        self.__locator()
        self.score = 0

    def __locator(self):
        self.x = random.randint(-1, FIELD - 1)
        self.y = random.randint(-1, FIELD - 1)

    def eaten(self):
        self.__locator()
        self.score += 1
