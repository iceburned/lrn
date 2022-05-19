from collections import deque


def negative_check(c, m):  # m - milk, c - chocolate
    if c[-1] < 0:          # check for negative number in both queues
        c.pop()
    if m[0] < 0:
        m.popleft()
    return c, m


def equal_remove(c, m):  # m - milk, c - chocolate
    c.pop()              # if equal removes them from queues
    m.popleft()
    return c, m


def count_shakes(flg, cnt):  # flg - flag, cnt - count
    cnt += 1                 # if function equal_remove pass, then 1 milkshake added to count
    if cnt == 5:
        flg = True
        return flg, cnt
    else:
        flg = False
        return flg, cnt


def elements_rotate(c, m):  # m - milk, c - chocolate
    m.append(m.popleft())   # logic when c and m are not equal in numbers
    c[-1] -= 5
    return c, m


'''
On the first line of input, you will receive the integers representing the chocolate, separated by  ", ". 
On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
'''


choco = deque(int(_) for _ in input().split(", "))
milk = deque(int(_) for _ in input().split(", "))
count = 0
flag = False
while choco and milk and not flag:
    if choco[-1] != milk[0]:
        choco, milk = negative_check(choco, milk)
    elif choco[-1] != milk[0]:
        choco, milk = elements_rotate(choco, milk)
    else:
        choco, milk = equal_remove(choco, milk)
        flag, count = count_shakes(flag, count)

choco = [str(_) for _ in choco]  # need to make int into strings for join( function to work
milk = [str(_) for _ in milk]  # need to make int into strings for join( function to work

if flag:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if choco:
    print("Chocolate: " + ', '.join(choco))
else:
    print("Chocolate: empty")
if milk:
    print("Milk: " + ', '.join(milk))
else:
    print("Milk: empty")
