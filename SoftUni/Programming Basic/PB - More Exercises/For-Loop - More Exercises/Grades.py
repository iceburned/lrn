students_count = int(input())

top = 0
good = 0
middle = 0
fail = 0
count = 0
sum_sum = 0
for _ in range(students_count):
    student = float(input())
    if student <= 2.99:
        fail += 1
        count += 1
        sum_sum += student
    elif 3.00 <= student <= 3.99:
        middle += 1
        count += 1
        sum_sum += student
    elif 4.00 <= student <= 4.99:
        good += 1
        count += 1
        sum_sum += student
    elif 5.00 <= student:
        top += 1
        count += 1
        sum_sum += student

top_average = top / count * 100
good_average = good / count * 100
middle_average = middle / count * 100
fail_average = fail / count * 100
average = sum_sum / students_count

print(f'Top students: {top_average:.2f}%\nBetween 4.00 and 4.99: {good_average:.2f}%'
      f'\nBetween 3.00 and 3.99: {middle_average:.2f}%\nFail: {fail_average:.2f}%'
      f'\nAverage: {average:.2f}')
