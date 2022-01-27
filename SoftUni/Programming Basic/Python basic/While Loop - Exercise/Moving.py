w = int(input())
length = int(input())
h = int(input())

s = w * h * length
s1 = 0
while s > s1:
    box = input()
    if box == "Done":
        break
    s1 += int(box)

sum_sum = abs(s1 - s)

if s1 >= s:
    print(f"No more free space! You need {sum_sum} Cubic meters more.")
else:
    print(f"{sum_sum} Cubic meters left.")
