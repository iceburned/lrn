count_hrisantemi = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
holiday = input()

hrisantemi = 0
roses = 0
tulips = 0

if season == "Spring" or season == "Summer":
    hrisantemi = 2.00
    roses = 4.10
    tulips = 2.50
elif season == "Autumn" or season == "Winter":
    hrisantemi = 3.75
    roses = 4.50
    tulips = 4.15
else:
    pass

price_hrisantemi = hrisantemi * count_hrisantemi
price_roses = roses * count_roses
price_tulips = tulips * count_tulips
price_bouquet = price_hrisantemi + price_roses + price_tulips
count_bouquet = count_hrisantemi + count_roses + count_tulips
if holiday == "Y":
    price_bouquet += price_bouquet * 0.15
if count_roses >= 10 and season == "Winter":
    price_bouquet -= price_bouquet * 0.10
if count_tulips > 7 and season == "Spring":
    price_bouquet -= price_bouquet * 0.05

if count_bouquet > 20:
    price_bouquet -= price_bouquet * 0.20
else:
    pass
price_bouquet1 = price_bouquet + 2
print(f'{price_bouquet1:.2f}')
