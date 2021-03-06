# finding rover position in matrix
def rover_position(mtx):  # mtx = field matrix
    for i in range(len(mtx)):
        if "E" in mtx[i]:
            ii = mtx[i].index("E")
            rover_row = i
            rover_col = ii
            return rover_row, rover_col


# finding next position according moving command
def get_next_position(r_row, r_col, comm):  # r_row -row, r_col - column, comm - direction
    if comm == "up":
        return r_row - 1, r_col
    if comm == "down":
        return r_row + 1, r_col
    if comm == "left":
        return r_row, r_col - 1
    if comm == "right":
        return r_row, r_col + 1


# relocating of rover when go outside matrix
def outside_position(r_row, r_col):  # r_row - row, r_col - column
    if r_row < 0:
        return 5, r_col
    elif r_row > 5:
        return 0, r_col
    elif r_col < 0:
        return r_row, 5
    elif r_col > 5:
        return r_row, 0
    return r_row, r_col


# compare deposits and return position
def deposits(rover_row, rover_col, field):  # r_row - row, r_col - column, field - field matrix
    if field[rover_row][rover_col] == "W":
        print(f"Water deposit found at ({rover_row}, {rover_col})")
        return "W"
    elif field[rover_row][rover_col] == "M":
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
        return "M"
    elif field[rover_row][rover_col] == "C":
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
        return "C"
    elif field[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        return "broke"


mtx = [input().split() for _ in range(6)]  # field matrix
commands = input().split(", ")  # series of commands
rover_row, rover_col = rover_position(mtx)  # finding rover position in matrix
all_materials = set()  # container for 3 materials for suitable planet

for c in commands:
    next_rover_row, next_rover_col = get_next_position(rover_row, rover_col, c)  # finding next position
    rover_row, rover_col = outside_position(next_rover_row, next_rover_col)  # relocating of rover when go outside matrx
    material = deposits(rover_row, rover_col, mtx)  # compare deposits and return position

    if material == "broke":
        break
    elif not material:
        continue
    else:
        all_materials.add(material)

if len(all_materials) >= 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
