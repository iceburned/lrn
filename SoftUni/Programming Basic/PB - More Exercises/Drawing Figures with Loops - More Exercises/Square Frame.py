# Program to draw a Python number triangle
s = int(input())
for i in range(1, s):
    row = "* "
    print(" " * (s - i) + row * i)
for n in range(s, 0, -1):
    row = "* "
    print(" " * (s - n) + row * n)
