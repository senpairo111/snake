import copy
import settings


class Snake:
    def __init__(self):
        self.snake_life = True
        self.snake_length_x = [settings.START_POINT_X]
        self.snake_length_y = [settings.START_POINT_Y]

    def __move(self, x_dir, y_dir):
        self.snake_length_y = [self.snake_length_y[0] + y_dir] + self.snake_length_y
        self.snake_length_x = [self.snake_length_x[0] + x_dir] + self.snake_length_x

    def move_up(self):
        self.__move(0, -1)

    def move_down(self):
        self.__move(0, 1)

    def move_right(self):
        self.__move(1, 0)

    def move_left(self):
        self.__move(-1, 0)

    def snake_mover(self):
        del self.snake_length_x[-1]
        del self.snake_length_y[-1]
