import sys


beginning = int(input())
ending = int(input())
magic_number = int(input())

count = 0
for a in range(beginning, ending + 1):
    for b in range(beginning, ending + 1):
        count += 1
        if a + b == magic_number:
            print(f"Combination N:{count} ({a} + {b} = {magic_number})")
            sys.exit()

print(f"{count} combinations - neither equals {magic_number}")
