first = input()
second = input()
sum_sum = 0
data = input()
for i in range(ord(first), ord(second)):
    for s in data:
        if chr(i) == s:
            sum_sum += int(i)
print(sum_sum)

