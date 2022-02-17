import math

students = int(input())
lectures = int(input())
bonus = int(input())
lst = []
student_attendances = []
if lectures > 0:
    for i in range(students):
        attendances = int(input())
        student_attendances.append(attendances)
        total_bonus = (attendances / lectures) * (5 + bonus)
        lst.append(math.ceil(total_bonus))
    max_value = max(student_attendances)
    index = student_attendances.index(max_value)
    print(f"Max Bonus: {lst[index]}.")
    print(f"The student has attended {max_value} lectures.")
else:
    print(f'Max Bonus: 0.\nThe student has attended 0 lectures.')
