from snake import field
from apple import s
from apple import Apple
import copy
copy_x = 8
copy_y = 8
lines_array = [["*"] * field for _ in range(field)]
last_m = "up"
a = Apple()
while s.snake_life:
    if s.snake_length_x[0] == a.x and s.snake_length_y[0] == a.y:
        a.eaten()
        s.snake_length_x.append(copy.deepcopy(copy_x))
        s.snake_length_y.append(copy.deepcopy(copy_y))
    print(a.score)
    snake_moved = False
    for i in lines_array:
        for y in s.snake_length_y:
            for x in s.snake_length_x:
                if lines_array[y] is i:
                    lines_array[y][x] = "O"
        if lines_array[a.y] is i:
            lines_array[a.y][a.x] = "A"
        display_line = '  '.join(i)
        print(display_line)

    m = input("insert left, right, up, or down here>> ")
    copy_x = copy.deepcopy(s.snake_length_x[s.snake_length])
    copy_y = copy.deepcopy(s.snake_length_y[s.snake_length])
    while not snake_moved:
        if m == "left":
            lines_array[copy_y][copy_x] = "*"
            s.move_left()
            last_m = m
            snake_moved = True
        elif m == "right":
            lines_array[copy_y][copy_x] = "*"
            s.move_right()
            last_m = m
            snake_moved = True
        elif m == "up":
            lines_array[copy_y][copy_x] = "*"
            s.move_up()
            last_m = m
            snake_moved = True
        elif m == "down":
            lines_array[copy_y][copy_x] = "*"
            s.move_down()
            last_m = m
            snake_moved = True
        else:
            m = last_m
        s.snake_mover()

        if s.x >= field or s.x <= -1 or s.y <= -1 or s.y >= field:
            s.snake_life = False

print("game over")
print(f"score {a.score}")
