from collections import deque

num = (int(input()))
queue = deque(int(_) for _ in input().split(' '))
print(max(queue))
while num > 0:
    if queue:
        if queue[0] <= num:
            num -= queue[0]
            queue.popleft()
        else:
            num = 0
    else:
        break
queue = list(queue)
if queue:
    print("Orders left: ", end='')
    print(*queue)
else:
    print("Orders complete")

