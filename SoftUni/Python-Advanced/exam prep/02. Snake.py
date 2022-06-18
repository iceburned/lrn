size = int(input())
mtx = [[s for s in input()] for _ in range(size)]


def position(matrix, search):
    for s in range(len(matrix)):
        for ss in range(len(matrix[s])):
            if matrix[s][ss] == search:
                return s, ss


def get_next_pos(snake_row, snake_col, direct):
    if direct == 'up':
        return snake_row - 1, snake_col
    elif direct == 'down':
        return snake_row + 1, snake_col
    elif direct == 'left':
        return snake_row, snake_col - 1
    elif direct == 'right':
        return snake_row, snake_col + 1


food = 0
while True:
    direction = input()
    snake_position = position(mtx, "S")
    mtx[snake_position[0]][snake_position[1]] = '.'
    new_sn_pos = get_next_pos(snake_position[0], snake_position[1], direction)
    try:
        if new_sn_pos[0] < 0 or new_sn_pos[1] < 0:
            raise IndexError
        if mtx[new_sn_pos[0]][new_sn_pos[1]] == "*":
            food += 1
            mtx[new_sn_pos[0]][new_sn_pos[1]] = 'S'
        elif mtx[new_sn_pos[0]][new_sn_pos[1]] == "B":
            mtx[new_sn_pos[0]][new_sn_pos[1]] = "."
            new_sn_pos = position(mtx, "B")
            mtx[new_sn_pos[0]][new_sn_pos[1]] = 'S'
        else:
            mtx[new_sn_pos[0]][new_sn_pos[1]] = 'S'
    except IndexError:
        print(f"Game over!\nFood eaten: {food}")
        break
    if food == 10:
        print(f"You won! You fed the snake.\nFood eaten: {food}")
        break
for s in mtx:
    print(''.join(s))
