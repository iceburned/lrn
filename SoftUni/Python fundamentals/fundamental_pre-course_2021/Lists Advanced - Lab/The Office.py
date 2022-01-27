employees = input().split()
employees = [int(_) for _ in employees]
factor = int(input())
filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))
if len(filtered) >= len(employees) / 2:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are not happy!')
