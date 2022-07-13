effort = 0
str_digit = []
cell = input().split('#')
water = int(input())
fire = 0
print('Cells:')
for s in cell:
    str_digit = s.split("=")
    int_str_digit = int(str_digit[1])
    if water <= 0:
        pass
    elif int_str_digit > water:
        pass
    elif str_digit[0] == 'High ':
        if int_str_digit in range(81, 126):
            water -= int_str_digit
            fire += int_str_digit
            effort += int_str_digit * 0.25
            print(f' - {int_str_digit}')
        else:
            pass
    elif str_digit[0] == 'Medium ':
        if int_str_digit in range(51, 81):
            water -= int_str_digit
            fire += int_str_digit
            effort += int_str_digit * 0.25
            print(f' - {int_str_digit}')
        else:
            pass
    elif str_digit[0] == 'Low ':
        if int_str_digit in range(1, 51):
            water -= int_str_digit
            fire += int_str_digit
            effort += int_str_digit * 0.25
            print(f' - {int_str_digit}')
        else:
            pass
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire}')


