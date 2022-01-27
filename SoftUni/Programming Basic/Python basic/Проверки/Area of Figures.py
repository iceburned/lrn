import math

shape = str(input())

if shape == "square":
    a = float(input())
    print(f'{(a * a):.3f}')
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    print(f'{(a * b):.3f}')
elif shape == "circle":
    a = float(input())
    print(f'{(math.pi * a**2):.3f}')
elif shape == "triangle":
    a = float(input())
    b = float(input())
    print(f'{((a / 2) * b):.3f}')
