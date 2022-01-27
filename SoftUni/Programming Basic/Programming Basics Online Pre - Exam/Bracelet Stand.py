pocket_money_per_day = float(input())
earned_money_per_day = float(input())
full_money_loss = float(input())
price_per_gift = float(input())

pocket_money = pocket_money_per_day * 5
earned_money = earned_money_per_day * 5
earned_sum = pocket_money + earned_money
money_loss = earned_sum - full_money_loss
if money_loss > price_per_gift:
    print(f"Profit: {money_loss:.2f} BGN, the gift has been purchased.")
else:
    sum_sum = price_per_gift - money_loss
    print(f"Insufficient money: {sum_sum:.2f} BGN.")
