from collections import deque


def calculate_nectar(bee, nectr, honey):  # if logic is satisfied then nectar is calculated
    b = bee[0]
    n = nectr[-1]
    h = honey[0]
    honey_made = 0
    if b == 0 or nectr == 0 and h == '/':
        pass
    else:
        honey_made = eval(f"{b}{h}{n}")
    return abs(honey_made)


def remove_elements(bee, nectr, honey):  # after calculate_nectar pass then remove corresponding elements
    bee.popleft()
    nectr.pop()
    honey.popleft()
    return bee, nectr, honey


def remove_nectar(n):  # after not satisfied conditions, only nectar is removed.
    n.pop()
    return n


'''
On the first line, you will be given the values of bees - integers, separated by a single space
On the second line, you will be given the nectar's values - integers, separated by a single space
On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a single space
'''

bees = deque(int(_) for _ in input().split(' '))
nectar = deque(int(_) for _ in input().split(' '))
honey_making = deque(_ for _ in input().split(' '))
honey_sum = 0
while bees and nectar:
    if bees[0] <= nectar[-1]:
        honey_sum += calculate_nectar(bees, nectar, honey_making)
        bees, nectar, honey_making = remove_elements(bees, nectar, honey_making)
    else:
        nectar = remove_nectar(nectar)

print(f"Total honey made: {honey_sum}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
