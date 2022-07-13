employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students = int(input())
count = 0
students_per_hour = employee1 + employee2 + employee3
hours = 0
while students > 0:
    hours += 1
    students -= students_per_hour
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")
