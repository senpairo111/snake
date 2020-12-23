from snake import field
from apple import s
from snake import Snake
from apple import Apple
lines_array = [["*"] * field for _ in range(field)]
last_m = "up"
a = Apple()
while s.snake_life or s.x >= field or s.x <= 0 or s.y <= 0 or s.y >= field:
    print(a.score)
    snake_moved = False
    for i in lines_array:
        if s.x >= field or s.x <= 0 or s.y <= 0 or s.y >= field:
            s.snake_life = False
        if lines_array[s.y] is i:
            lines_array[s.y][s.x] = "O"
        if lines_array[a.y] is i:
            lines_array[a.y][a.x] = "$"
        display_line = '  '.join(i)
        print(display_line)

    m = input("insert left, right, up, or down here")
    while not snake_moved:
        if m == "left":
            lines_array[s.y][s.x] = "*"
            s.move_left()
            last_m = m
            snake_moved = True
        elif m == "right":
            lines_array[s.y][s.x] = "*"
            s.move_right()
            last_m = m
            snake_moved = True
        elif m == "up":
            lines_array[s.y][s.x] = "*"
            s.move_up()
            last_m = m
            snake_moved = True
        elif m == "down":
            lines_array[s.y][s.x] = "*"
            s.move_down()
            last_m = m
            snake_moved = True
        else:
            m = last_m
        if s.x == a.x and s.y == a.y:
            a.eaten()
print("game over")
