def char_in_range(a1, b1):
    for i in range(ord(a1) + 1, ord(b1)):
        print(chr(i), end=' ')


a = input()
b = input()

char_in_range(a, b)
