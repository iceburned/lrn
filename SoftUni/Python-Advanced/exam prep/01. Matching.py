from collections import deque

male = [int(_) for _ in input().split(' ')]
female = deque(int(_) for _ in input().split(' '))


matches = 0
while male and female:
    m = male.pop()
    f = female.popleft()
    if m <= 0:
        female.appendleft(f)
        continue
    if f <= 0:
        male.append(m)
        continue
    if m % 25 == 0:
        female.appendleft(f)
        m = male.pop()
        continue
    if f % 25 == 0:
        male.append(m)
        f = female.popleft()
        continue
    if m == f:
        matches += 1
    else:
        male.append(m - 2)

male.reverse()
print(f'Matches: {matches}')
if male:
    print(f'Males left: {", ".join(map(str, male))}')
else:
    print("Males left: none")
if female:
    print(f'Females left: {", ".join((map(str, female)))}')
else:
    print("Females left: none")
