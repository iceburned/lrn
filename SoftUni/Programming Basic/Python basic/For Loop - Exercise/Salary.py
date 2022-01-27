tabs = int(input())
salary = int(input())

for _ in range(0, tabs):
    web_name = str(input())
    if web_name == "Facebook":
        salary -= 150
    elif web_name == "Instagram":
        salary -= 100
    elif web_name == "Reddit":
        salary -= 50
    else:
        pass

    if salary <= 0:
        print("You have lost your salary.")
        break
    else:
        pass

if salary > 0:
    print(salary)
