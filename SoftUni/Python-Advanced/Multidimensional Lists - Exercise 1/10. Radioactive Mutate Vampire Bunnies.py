def get_next_pos(row, col, command):
    if command == "U":
        return row - 1, col
    if command == "D":
        return row + 1, col
    if command == "L":
        return row, col - 1
    if command == "R":
        return row, col + 1


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(_) for _ in input().split()]

bunnies = set()
player_row = 0
player_col = 0

matrix = []

for row in range(rows):
    row_elements = list(input())
    for col in range(cols):
        if row_elements[col] == "P":
            player_row = row
            player_col = col
        elif row_elements[col] == "B":
            bunnies.add(f"{row} {col}")

print(player_row, player_col)
print(bunnies)

commands = input()

won = False
dead = False




for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)
    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == "B":
        dead = True
