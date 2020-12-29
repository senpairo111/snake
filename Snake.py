import copy

class Snake:
    def __init__(self):
        self.x = 8
        self.y = 8
        self.snake_life = True
        self.snake_length = 0
        self.snake_length_x = [self.x]
        self.snake_length_y = [self.y]
        self.last_move_y = 1
        self.last_move_x = 1
        
    def move_up(self):
        self.snake_length_y[0] -= 1
        self.last_move_y = -1

    def move_down(self):
        self.snake_length_y[0] += 1
        self.last_move_y = 1

    def move_right(self):
        self.snake_length_x[0] += 1
        self.last_move_x = 1

    def move_left(self):
        self.snake_length_x[0] -= 1
        self.last_move_x = -1

    def snake_mover(self):
        for i in range(1, self.snake_length):
            self.snake_length_x[self.snake_length - i] = copy.deepcopy(self.snake_length_x[self.snake_length - i + 1])
            self.snake_length_y[self.snake_length - i] = copy.deepcopy(self.snake_length_y[self.snake_length - i + 1])







