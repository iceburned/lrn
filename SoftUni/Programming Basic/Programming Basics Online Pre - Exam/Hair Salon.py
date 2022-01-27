goal = int(input())

earned_money = 0
while True:
    if earned_money >= goal:
        break
    type_haircut = input()
    if type_haircut == 'closed':
        break
    person = input()
    if type_haircut == 'haircut':
        if person == 'mens':
            earned_money += 15
        elif person == 'ladies':
            earned_money += 20
        elif person == 'kids':
            earned_money += 10
    elif type_haircut == 'color':
        if person == 'touch up':
            earned_money += 20
        elif person == 'full color':
            earned_money += 30
sum_sum = goal - earned_money
if goal <= earned_money:
    print("You have reached your target for the day!")
    print(f"Earned money: {earned_money}lv.")
else:

    print(f"Target not reached! You need {sum_sum}lv. more.")
    print(f"Earned money: {earned_money}lv.")
