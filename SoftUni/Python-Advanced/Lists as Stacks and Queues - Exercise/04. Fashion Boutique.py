clothes = [int(_) for _ in input().split(" ")]
rack = int(input())
sum_sum = 0
count = 1
while clothes:
    if rack > sum_sum and not sum_sum + clothes[-1] > rack:
        sum_sum += clothes.pop()
    elif rack == sum_sum:
        count += 1
        sum_sum = 0

    else:
        count += 1
        sum_sum = 0
        sum_sum += clothes.pop()
print(count)
