def calculations(a, b, c):
    if a == 'multiply':
        return b * c
    elif a == 'divide':
        return b // c
    elif a == 'add':
        return b + c
    elif a == 'subtract':
        return b - c

print(calculations(a = input(), b = int(input()), c = int(input())))
