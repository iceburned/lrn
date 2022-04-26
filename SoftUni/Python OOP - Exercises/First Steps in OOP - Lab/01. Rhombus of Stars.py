def stars_up(num):
    for row in range(1, num + 1):
        for space in range(num - row):
            print(" ", end='')
        for star in range(1, row):
            print("*", end=' ')
        print("*")


def stars_down(num):
    for row in range(num - 1, 0, -1):
        for space in range(num - row):
            print(" ", end='')
        for star in range(1, row):
            print("*", end=' ')
        print("*")


def stars(n):
    stars_up(n)
    stars_down(n)


data = int(input())
stars(data)
