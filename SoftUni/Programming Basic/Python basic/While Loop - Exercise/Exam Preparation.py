low_grade = int(input())

exec = ''
exercise_name = ''
count_exercises = 0
exercises_sum = 0
count_grade = 0
while True:
    exercise_name = input()
    if exercise_name == "Enough":
        sum_sum = exercises_sum / count_exercises
        print(f'Average score: {sum_sum:.2f}')
        print(f"Number of problems: {count_exercises}")
        print(f"Last problem: {exec}")
        break
    exec = exercise_name

    grade = int(input())
    count_exercises += 1
    exercises_sum += grade
    if grade <= 4:
        count_grade += 1
    if low_grade == count_grade:
        print(f"You need a break, {count_grade} poor grades.")
        break
