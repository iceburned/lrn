import math


def coordinates(coord):
    a = math.sqrt((coord[2] - coord[0])**2 + (coord[3] - coord[1])**2)
    b = math.sqrt((coord[6] - coord[4])**2 + (coord[7] - coord[5])**2)
    if a < b:
        if sum((abs(coord[6]), abs(coord[7]))) < sum((abs(coord[4]), abs(coord[5]))):
            return (f'({math.floor(coord[6])}, {math.floor(coord[7])})'
                f'({math.floor(coord[4])}, {math.floor(coord[5])})')
        else:
            return (f'({math.floor(coord[4])}, {math.floor(coord[5])})'
                    f'({math.floor(coord[6])}, {math.floor(coord[7])})')
    else:
        if sum((abs(coord[2]), abs(coord[3]))) < sum((abs(coord[0]), abs(coord[1]))):
            return (f'({math.floor(coord[2])}, {math.floor(coord[3])})'
                  f'({math.floor(coord[0])}, {math.floor(coord[1])})')
        else:
            return (f'({math.floor(coord[0])}, {math.floor(coord[1])})'
                    f'({math.floor(coord[2])}, {math.floor(coord[3])})')


co = []
for i in range(8):
    co.append(float(input()))
print(coordinates(co))
