month = input()
sleep_in_hotel = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 > sleep_in_hotel <= 14:
        studio -= studio * 0.05
    elif sleep_in_hotel > 14:
        studio -= studio * 0.30
        apartment -= apartment * 0.10
    else:
        pass
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if sleep_in_hotel <= 14:
        pass
    else:
        studio -= studio * 0.20
        apartment -= apartment * 0.10
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if sleep_in_hotel <= 14:
        pass
    else:
        apartment -= apartment * 0.10
else:
    pass

print(f'Apartment: {(apartment * sleep_in_hotel):.2f} lv.')
print(f'Studio: {(studio * sleep_in_hotel):.2f} lv.')
