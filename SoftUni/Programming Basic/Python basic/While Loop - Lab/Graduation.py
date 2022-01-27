pupil_name = input()
evaluation = 0
class_grade = 0
dismiss = 0
while True:
    grade = float(input())
    class_grade += 1
    if grade >= 4.00 and class_grade < 12:
        evaluation += grade
    elif class_grade == 12:
        evaluation += grade
        average_grade = evaluation / class_grade
        print(f"{pupil_name} graduated. Average grade: {average_grade:.2f}")
        break
    else:
        dismiss += 1
        if dismiss >= 1:
            print(f"{pupil_name} has been excluded at {class_grade} grade")
            break
