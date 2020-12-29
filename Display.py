from settings import FIELD
from Apple import snake
from Apple import Apple
import copy

# Global Variables
copy_x = 8
copy_y = 8
lines_array = [["*"] * FIELD for _ in range(FIELD)]
last_movement = "up"
apple = Apple()


while snake.snake_life:
    if snake.snake_length_x[0] == apple.x and snake.snake_length_y[0] == apple.y:
        apple.eaten()
        snake.snake_length_x.append(copy.deepcopy(copy_x))
        snake.snake_length_y.append(copy.deepcopy(copy_y))
    print(apple.score)
    snake.snake_moved = False
    for i in lines_array:
        for y in snake.snake_length_y:
            for x in snake.snake_length_x:
                if lines_array[y] is i:
                    lines_array[y][x] = "O"
        if lines_array[apple.y] is i:
            lines_array[apple.y][apple.x] = "A"
        display_line = '  '.join(i)
        print(display_line)

    m = input("insert left, right, up, or down here>> ")
    copy_x = copy.deepcopy(snake.snake_length_x[snake.snake_length])
    copy_y = copy.deepcopy(snake.snake_length_y[snake.snake_length])


    while not snake.snake_moved:
        if m == "left":
            lines_array[copy_y][copy_x] = "*"
            snake.move_left()
            last_movement = m
        elif m == "right":
            lines_array[copy_y][copy_x] = "*"
            snake.move_right()
            last_movement = m
        elif m == "up":
            lines_array[copy_y][copy_x] = "*"
            snake.move_up()
            last_movement = m
        elif m == "down":
            lines_array[copy_y][copy_x] = "*"
            snake.move_down()
            last_movement = m
        else:
            m = last_movement
        snake.snake_mover()

        if snake.x >= FIELD or snake.x <= -1 or snake.y <= -1 or snake.y >= FIELD:
            snake.snake_life = False

print("game over")
print(f"score {apple.score}")
