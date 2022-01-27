n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif num >= 800:
        p5 += 1

p11 = p1 / n * 100
p22 = p2 / n * 100
p33 = p3 / n * 100
p44 = p4 / n * 100
p55 = p5 / n * 100

print(f'{p11:.2f}%')
print(f'{p22:.2f}%')
print(f'{p33:.2f}%')
print(f'{p44:.2f}%')
print(f'{p55:.2f}%')
