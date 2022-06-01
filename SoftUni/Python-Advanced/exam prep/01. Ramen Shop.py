from collections import deque

bows_ramen = deque(int(_) for _ in input().split(", "))
customers = deque(int(_) for _ in input().split(", "))

while bows_ramen and customers:
    last_ramen = bows_ramen.pop()
    first_customer = customers.popleft()
    if last_ramen == first_customer:
        continue
    elif last_ramen > first_customer:
        temp_num = last_ramen - first_customer
        bows_ramen.append(temp_num)
    elif first_customer > last_ramen:
        temp_num = first_customer - last_ramen
        customers.appendleft(temp_num)

if not bows_ramen and not customers:
    print("Great job! You served all the customers.")
elif bows_ramen:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(map(str, bows_ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
