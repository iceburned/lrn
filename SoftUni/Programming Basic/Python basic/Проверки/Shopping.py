budget_Peter = float(input())

videocards = int(input())
videocards_sum = videocards * 250

CPU = int(input())
CPU_price = videocards_sum * 0.35
CPU_sum = CPU * CPU_price

RAM = int(input())
RAM_price = videocards_sum * 0.10
RAM_sum = RAM * RAM_price

sum_sum = videocards_sum + CPU_sum + RAM_sum
sum_sum1 = sum_sum
if videocards >= CPU:
    sum_discount = sum_sum * 0.15
    sum_sum1 = sum_sum - sum_discount
if sum_sum1 <= budget_Peter:
    money = budget_Peter - sum_sum1
    print(f'You have {money:.2f} leva left!')
else:
    money1 = sum_sum1 - budget_Peter
    print(f"Not enough money! You need {money1:.2f} leva more!")

