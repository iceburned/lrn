def position(mtx_pos):
    for i in range(len(mtx_pos)):
        if "B" in mtx_pos[i]:
            index = mtx_pos[i].index("B")
            pos = i, index
            return pos


def up(mtx_up, rabbit_pos):
    eggs = 0
    road_rabbit = []
    for i in range(rabbit_pos[0]-1, -1, -1):
        if not mtx_up[i][rabbit_pos[1]] == "X":
            eggs += mtx_up[i][rabbit_pos[1]]
            road_rabbit.append([i, rabbit_pos[1]])
        else:
            return eggs, road_rabbit
    return eggs, road_rabbit


def right(mtx_right, rabbit_pos):
    eggs = 0
    road_rabbit = []
    for i in range(rabbit_pos[1]+1, len(mtx_right[rabbit_pos[0]])):
        if not mtx_right[rabbit_pos[0]][i] == "X" :
            eggs += mtx_right[rabbit_pos[0]][i]
            road_rabbit.append([rabbit_pos[0], i])
        else:
            return eggs, road_rabbit
    return eggs, road_rabbit


def down(mtx_down, rabbit_pos):
    eggs = 0
    road_rabbit = []
    for i in range(rabbit_pos[0]+1, len(mtx_down)):
        if not mtx_down[i][rabbit_position[1]] == "X":
            eggs += mtx_down[i][rabbit_position[1]]
            road_rabbit.append([i, rabbit_pos[1]])
        else:
            return eggs, road_rabbit
    return eggs, road_rabbit


def left(mtx_left, rabbit_pos):
    eggs = -0
    road_rabbit = []
    for i in range(rabbit_pos[1]-1, -1, -1):
        if not mtx_left[rabbit_pos[0]][i] == "X":
            eggs += mtx_left[rabbit_pos[0]][i]
            road_rabbit.append([rabbit_pos[0], i])
        else:
            return eggs, road_rabbit
    return eggs, road_rabbit


mtx = [[s for s in input().split()] for _ in range(int(input()))]
mtx = [[s if s.isalpha() else int(s) for s in _] for _ in mtx]
rabbit_position = position(mtx)

biggest_eggs = -1000
road = []
direction = ""

eggs_up, road_up = up(mtx, rabbit_position)
if eggs_up > biggest_eggs:
    biggest_eggs = eggs_up
    road = road_up
    direction = "up"

eggs_right, road_right = right(mtx, rabbit_position)
if eggs_right > biggest_eggs:
    biggest_eggs = eggs_right
    road = road_right
    direction = "right"

eggs_down, road_down = down(mtx, rabbit_position)
if eggs_down > biggest_eggs:
    biggest_eggs = eggs_down
    road = road_down
    direction = "down"

eggs_left, road_left = left(mtx, rabbit_position)
if eggs_left > biggest_eggs:
    biggest_eggs = eggs_left
    road = road_left
    direction = "left"

print(direction)
for s in road:
    print(s)
print(biggest_eggs)

# def is_inside(r, c, size):
#     return 0 <= r < size and 0 <= c < size
#
#
# def position(mtx_pos):
#     for i in range(len(mtx_pos)):
#         if "B" in mtx_pos[i]:
#             index = mtx_pos[i].index("B")
#             pos = i, index
#             return pos
#
#
# size = int(input())
# mtx = [[s for s in input().split()] for _ in range(size)]
# mtx = [[s if s.isalpha() else int(s) for s in _] for _ in mtx]
# rabbit_position = position(mtx)
# directions = {
#     "right": lambda r, c: (r, c + 1),
#     "left": lambda r, c: (r, c - 1),
#     "up": lambda r, c: (r - 1, c),
#     "down": lambda r, c: (r + 1, c)
# }
#
# max_eggs = 0
# best_direction = ''
# best_path = []
#
# for directions, step in directions.items():
#     eggs = 0
#     current_row, current_col = rabbit_position[0], rabbit_position[1]
#     path = []
#     while True:
#         next_row, next_col = step(current_row, current_col)
#         if not is_inside(current_row, current_col, size):
#             break
#         if mtx[next_row][next_col] == "X":
#             break
#
#         eggs += int(mtx[next_row][next_col])
#         path.append([current_row, current_col])
#     if eggs > max_eggs:
#         max_eggs = eggs
#         best_direction = directions
#         best_path = path
#
#
# print(best_path)
# for step in best_path:
#     print(step)
# print(max_eggs)
