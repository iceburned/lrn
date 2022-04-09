mtx = []
num_1, num_2 = [int(_) for _ in input().split(", ")]
sum_sum = 0
for s in range(num_1):
    temp_sum = [int(_) for _ in input().split(", ")]
    mtx.append(temp_sum)
    sum_sum += sum(temp_sum)
print(sum_sum)
print(mtx)
