from collections import deque

customers = deque(int(_) for _ in input().split(', '))
taxis = [int(_) for _ in input().split(', ')]
total_time = 0

while customers and taxis:
    guy = customers.popleft()
    car = taxis.pop()
    a = 1
    if car >= guy:
        total_time += guy
    elif car < guy:
        customers.appendleft(guy)

customers = [str(_) for _ in customers]

if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join(customers)}')
