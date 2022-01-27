lines = int(input())
even_num = []
odd_num = []
negative_num = []
positive_num = []
for _ in range(0, lines + 1):
    str_data = input()
    if str_data == 'even':
        print(even_num)
        break
    elif str_data == 'odd':
        print(odd_num)
        break
    elif str_data == 'negative':
        print(negative_num)
        break
    elif str_data == 'positive':
        print(positive_num)
        break
    str_data = int(str_data)
    if str_data % 2 == 0:
        even_num.append(str_data)
    elif str_data % 2 != 0:
        odd_num.append(str_data)
    if str_data >= 0:
        positive_num.append(str_data)
    else:
        negative_num.append(str_data)
