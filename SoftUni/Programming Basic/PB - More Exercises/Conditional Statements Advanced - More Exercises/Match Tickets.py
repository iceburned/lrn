budget = float(input())
type_ticket = input()
mob = int(input())

budget_transport = 0
if 1 <= mob <= 4:
    budget_transport = budget - (budget * 0.75)
elif 5 <= mob <= 9:
    budget_transport = budget - (budget * 0.60)
elif 10 <= mob <= 24:
    budget_transport = budget - (budget * 0.50)
elif 25 <= mob <= 49:
    budget_transport = budget - (budget * 0.40)
else:
    budget_transport = budget - (budget * 0.25)

sum_price = 0
if type_ticket == "VIP":
    sum_price = 499.99 * mob
elif type_ticket == "Normal":
    sum_price = 249.99 * mob

sum_sum = abs(budget_transport - sum_price)

if sum_price <= budget_transport:
    print(f'Yes! You have {sum_sum:.2f} leva left.')
else:
    print(f'Not enough money! You need {sum_sum:.2f} leva.')
