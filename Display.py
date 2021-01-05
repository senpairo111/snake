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
    print(apple.score)
    for j in range(len(snake.snake_length_x)):
        lines_array[snake.snake_length_y[j]][snake.snake_length_x[j]] = "O"
    lines_array[apple.y][apple.x] = "A"
    for i in lines_array:
        display_line = '  '.join(i)
        print(display_line)

    m = input("insert left, right, up, or down here>> ")
    copy_x = snake.snake_length_x[-1]
    copy_y = snake.snake_length_y[-1]

    if m not in ["up", "down", "left", "right"]:
        m = last_movement
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
    if snake.snake_length_x[0] == apple.x and snake.snake_length_y[0] == apple.y:
        apple.eaten()
    else:
        snake.snake_mover()

    if snake.snake_length_x[0] >= FIELD or snake.snake_length_x[0] <= -1 or snake.snake_length_y[0] <= -1 or \
            snake.snake_length_y[0] >= FIELD:
        snake.snake_life = False


print("game over")
print(f"score {apple.score}")
