first_player, second_player = input().split(', ')
board = [input().split(' ') for _ in range(6)]


def coordinates(cord):
    r, c = cord.strip("()").split(', ')
    return int(r), int(c)


data = input()
rest = []
while data:
    row, col = coordinates(data)
    if rest:
        if rest[0] == first_player:
            rest.pop(0)
            first_player, second_player = second_player, first_player
            data = input()
            continue
    if board[row][col] == "W":
        print(f"{first_player} hits a wall and needs to rest.")
        rest.append(first_player)
    elif board[row][col] == "T":
        print(f"{first_player} is out of the game! The winner is {second_player}.")
        break
    elif board[row][col] == "E":
        winner = first_player
        print(f"{first_player} found the Exit and wins the game!")
        break
    first_player, second_player = second_player, first_player
    data = input()

