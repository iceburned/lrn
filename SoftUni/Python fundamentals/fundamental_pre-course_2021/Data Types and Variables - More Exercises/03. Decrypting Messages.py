key = int(input())
lines = int(input())
for _ in range(lines):
    pass_letter = input()
    letter = ord(pass_letter) + key
    print(chr(letter), end='')
