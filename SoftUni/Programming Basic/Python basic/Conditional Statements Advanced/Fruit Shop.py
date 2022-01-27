fruit = str(input())
day = str(input())
quantity = float(input())
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":

    if fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes":
        asd = 0
        if fruit == "banana":
            asd = 2.50
        elif fruit == "apple":
            asd = 1.20
        elif fruit == "orange":
            asd = 0.85
        elif fruit == "grapefruit":
            asd = 1.45
        elif fruit == "kiwi":
            asd = 2.70
        elif fruit == "pineapple":
            asd = 5.50
        elif fruit == "grapes":
            asd = 3.85
        sum_sum = quantity * asd
        print(f'{sum_sum:.2f}')
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes":
        asd = 0
        if fruit == "banana":
            asd = 2.70
        elif fruit == "apple":
            asd = 1.25
        elif fruit == "orange":
            asd = 0.90
        elif fruit == "grapefruit":
            asd = 1.60
        elif fruit == "kiwi":
            asd = 3.00
        elif fruit == "pineapple":
            asd = 5.60
        elif fruit == "grapes":
            asd = 4.20
        sum_sum = quantity * asd
        print(f'{sum_sum:.2f}')
    else:
        print("error")
else:
    print("error")
