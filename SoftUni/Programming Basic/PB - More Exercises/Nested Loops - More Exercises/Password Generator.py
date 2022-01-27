num1 = int(input())
num2 = int(input())

letter = 97 + num2
for a in range(1, num1 + 1):
    for b in range(1, num1 + 1):
        for c in range(97, letter):
            for d in range(97, letter):
                for e in range(1, num1 + 1):
                    if e > a and e > b:
                        print(f'{a}{b}{chr(c)}{chr(d)}{e}', end=' ')

