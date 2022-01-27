final_time = str(input())
type_ticket = str(input())
tickets = int(input())
picture_trophy = str(input())
ticket_price = 0
final_time1 = 0
bonus = False
ticket_one = 0

if 'Quarter final' == final_time:
    if 'Standard' == type_ticket:
        final_time1 = 55.50
    elif 'Premium' == type_ticket:
        final_time1 = 105.20
    elif 'VIP' == type_ticket:
        final_time1 = 105.20
elif 'Semi final' == final_time:
    if 'Standard' == type_ticket:
        final_time1 = 75.88
    elif 'Premium' == type_ticket:
        final_time1 = 125.22
    elif 'VIP' == type_ticket:
        final_time1 = 300.40
elif 'Final' == final_time:
    if 'Standard' == type_ticket:
        final_time1 = 110.10
    elif 'Premium' == type_ticket:
        final_time1 = 160.66
    elif 'VIP' == type_ticket:
        final_time1 = 400
ticket_price = final_time1 * tickets
if ticket_price > 4000:
    ticket_price -= (ticket_price * 0.25)
    bonus = False
elif 2500 < ticket_price < 4000:
    ticket_price -= (ticket_price * 0.10)
    bonus = True
if 'Y' == picture_trophy and bonus:
    ticket_one += (tickets * 40)

sum_sum = ticket_price + ticket_one

print(f'{sum_sum:.2f}')
