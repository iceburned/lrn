import math


def cartesian(a1, b1, a2, b2):
    dest_1 = math.sqrt(a1**2 + b1**2)
    dest_2 = math.sqrt(a2**2 + b2**2)
    if dest_1 < dest_2:
        return a1, b1
    elif dest_1 > dest_2:
        return a2, b2
    else:
        return a1, b1


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
answer = cartesian(x1, y1, x2, y2)

print(f'({math.floor(answer[0])}, {math.floor(answer[1])})')
