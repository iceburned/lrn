group = int(input())
season = (input())
fishermans = int(input())
boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
else:
    boat_price = 2600

if fishermans <= 6:
    boat_price -= boat_price * 0.10
elif 7 <= fishermans <= 11:
    boat_price -= boat_price * 0.15
elif fishermans >= 12:
    boat_price -= boat_price * 0.25

if fishermans % 2 == 0 and season != "Autumn":
    boat_price -= boat_price * 0.05

sum_sum = abs(group - boat_price)

if group < boat_price:
    print(f'Not enough money! You need {sum_sum:.2f} leva.')
else:
    print(f'Yes! You have {sum_sum:.2f} leva left.')
