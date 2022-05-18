from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque(int(_) for _ in input().split(' '))
locks = deque(int(_) for _ in input().split(' '))
intelligence_value = int(input())
bullets_count = 0
reload_count = 1
while any(bullets) and any(locks):
    action = locks[0] - bullets[-1]
    if action >= 0:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    bullets.pop()
    bullets_count += 1
    if reload_count % gun_barrel_size == 0:
        if any(bullets):
            print("Reloading!")
            reload_count += 1
    else:
        reload_count += 1
bullets_sum = intelligence_value - bullets_count * bullet_price
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")

else:
    print(f"{len(bullets)} bullets left. Earned ${bullets_sum}")
