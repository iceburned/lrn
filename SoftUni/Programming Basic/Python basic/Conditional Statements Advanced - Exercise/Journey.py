budget = float(input())
season = input()

budget1 = 0
place = ''
sleep = ''
if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        budget1 = budget * 0.30
        sleep = "Camp"
    elif season == "winter":
        budget1 = budget * 0.70
        sleep = "Hotel"
elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        budget1 = budget * 0.40
        sleep = "Camp"
    elif season == "winter":
        budget1 = budget * 0.80
        sleep = "Hotel"
else:
    place = "Europe"
    budget1 = budget * 0.90
    sleep = "Hotel"

budget2 = budget - budget1
print(f'Somewhere in {place}')
print(f'{sleep} - {budget1:.2f}')

