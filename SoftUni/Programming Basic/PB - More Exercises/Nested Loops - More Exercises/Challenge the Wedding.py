import sys

man = int(input())
women = int(input())
table_max = int(input())

count = 0
for a in range(1, man + 1):
    for b in range(1, women + 1):
        print(f'({a} <-> {b})', end=' ')
        count += 1
        if count >= table_max:
            sys.exit()
