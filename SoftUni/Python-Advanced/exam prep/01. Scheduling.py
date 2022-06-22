jobs = [int(_) for _ in input().split(', ')]
idx = int(input())
sum_sum = 0
for s in range(1, jobs[idx]+1):
    sum_sum += s * jobs.count(s)
print(sum_sum)
