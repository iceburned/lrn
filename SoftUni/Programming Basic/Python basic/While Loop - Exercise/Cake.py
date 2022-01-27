h = int(input())
w = int(input())

s = h * w

while s > 0:
    piece = input()
    if piece == "STOP":
        break
    s -= int(piece)


if s <= 0:
    print(f"No more cake left! You need {abs(s)} pieces more.")
else:
    print(f"{s} pieces are left.")
