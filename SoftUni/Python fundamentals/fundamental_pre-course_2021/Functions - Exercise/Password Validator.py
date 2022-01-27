def pass_validator(num1):
    num_digit = 0
    flag = True
    for s in num1:
        if s.isnumeric():
            num_digit += 1
    if not len(num1) in range(6, 11):
        flag = False
        print('Password must be between 6 and 10 characters')
    if not num1.isalnum():
        flag = False
        print('Password must consist only of letters and digits')
    if num_digit < 2:
        flag = False
        print('Password must have at least 2 digits')
    if flag:
        print('Password is valid')


pass_validator(input())
