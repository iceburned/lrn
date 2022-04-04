from collections import deque

data = deque(_ for _ in input().split(' '))
count = int(input())
while len(data) > 1:
    data.rotate(-count)
    print(f"Removed {data.pop()}")
print(f"Last is {''.join(data)}")
