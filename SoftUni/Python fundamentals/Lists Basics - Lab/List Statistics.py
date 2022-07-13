count = int(input())

odd_list = []
even_list = []
even_count = 0
odd_sum = 0
for _ in range(0, count):
    num = int(input())
    if num >= 0:
        even_count += 1
        even_list.append(num)
    else:
        odd_list.append(num)
        odd_sum += num
print(f'{even_list}\n{odd_list}\nCount of positives: {even_count}'
      f'\nSum of negatives: {odd_sum}')
