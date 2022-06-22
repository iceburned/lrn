from collections import deque

orders = deque(int(_) for _ in input().split(', '))
employee = [int(_) for _ in input().split(', ')]

total_pizza = 0
while orders and employee:
    o = orders.popleft()
    e = employee.pop()
    if o <= 0:
        employee.append(e)
        continue
    if o > 10:
        employee.append(e)
        continue
    if o <= e:
        total_pizza += o
    elif o > e:
        total_pizza += e
        orders.appendleft(o - e)
if orders:
    print(f"Not all orders are completed.\nOrders left: {', '.join(map(str, orders))}")
else:
    print(f"All orders are successfully completed!\nTotal pizzas made: {total_pizza}\n"
          f"Employees: {', '.join(map(str, employee))}")
