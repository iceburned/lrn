
mtx_size = [[int(i) for i in input().split(" ")] for _ in range(int(input()))]
# bomb_position = tuple(tuple(int(i) for i in _.split(",")) for _ in input().split(' '))

def get_children(mtx_size, row, col):
    possible_childrens = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]

    result = []
    for children_row, children_col in possible_childrens:
        if 0 <= children_row < len(mtx_size) and 0 <= children_col < len(mtx_size) and mtx_size[children_row][children_col] > 0:
            result.append([children_row, children_col])
    return result


for i in input().split():
    row, col = [int(_) for _ in i.split(",")]
    power = mtx_size[row][col]

    if power <= 0:
        continue

    mtx_size[row][col] = 0

    children = get_children(mtx_size, row, col)
    for children_row, children_col in children:
        mtx_size[children_row][children_col] -= power

alive_cells_count = 0
alive_cells_sum = 0

for row in mtx_size:
    for el in row:
        if el > 0:
            alive_cells_count += 1
            alive_cells_sum += el

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")

for row in mtx_size:
    print(*row, sep=" ")


