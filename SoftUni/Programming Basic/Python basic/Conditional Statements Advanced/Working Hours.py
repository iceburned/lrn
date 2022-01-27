day = int(input())
week = str(input())
if week == "Monday" or week == "Tuesday" or week == "Wednesday" or week == "Thursday" or week == "Friday" or week == "Saturday":
    if 10 <= day <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")
