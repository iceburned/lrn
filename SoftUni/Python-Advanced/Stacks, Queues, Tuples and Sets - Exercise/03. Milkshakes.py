from collections import deque

choco = deque(int(_) for _ in input().split(", "))
milk = deque(int(_) for _ in input().split(", "))
while choco and milk:
    chocolate = choco[-1]
    milk_cup = milk[0]
    if chocolate == milk_cup:
        choco.pop()
        milk.popleft()
    else:
        if choco[-1] <= 0:
            milk.append(milk.popleft())

            choco.pop()
            choco[-1] -= 5
a = 1