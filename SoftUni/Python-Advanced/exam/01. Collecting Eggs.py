from collections import deque

eggs = deque(int(_) for _ in input().split(', '))
paper = deque(int(_) for _ in input().split(', '))

box = 0

while eggs and paper:
    e = eggs.popleft()
    p = paper.pop()

    if e <= 0:
        paper.append(p)

    elif e == 13:
        first_paper = paper.popleft()
        paper.appendleft(p)
        paper.append(first_paper)
    elif e + p <= 50:
        box += 1
    elif e + p > 50:
        pass
if box >= 1:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if paper:
    print(f"Pieces of paper left: {', '.join(map(str, paper))}")
