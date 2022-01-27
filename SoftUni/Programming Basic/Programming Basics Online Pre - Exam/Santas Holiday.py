days_to_stay = int(input()) - 1
room_type = input()
attitude = input()

place_to_stay = 0
if days_to_stay < 10:
    if room_type == 'room for one person':
        place_to_stay += 18.00 * days_to_stay
    elif room_type == 'apartment':
        place_to_stay += days_to_stay * 25.00 - ((days_to_stay * 25.00) * 0.3)
    elif room_type == 'president apartment':
        place_to_stay += days_to_stay * 35 - ((days_to_stay * 35) * 0.1)
elif 10 <= days_to_stay <= 15:
    if room_type == 'room for one person':
        place_to_stay += 18.00 * days_to_stay
    elif room_type == 'apartment':
        place_to_stay += days_to_stay * 25.00 - ((days_to_stay * 25.00) * 0.35)
    elif room_type == 'president apartment':
        place_to_stay += days_to_stay * 35 - ((days_to_stay * 35) * 0.15)
elif days_to_stay > 15:
    if room_type == 'room for one person':
        place_to_stay += 18.00 * days_to_stay
    elif room_type == 'apartment':
        place_to_stay += days_to_stay * 25.00 - ((days_to_stay * 25.00) * 0.5)
    elif room_type == 'president apartment':
        place_to_stay += days_to_stay * 35 - ((days_to_stay * 35) * 0.2)

if attitude == 'positive':
    place_to_stay = place_to_stay + (place_to_stay * 0.25)
else:
    place_to_stay = place_to_stay - (place_to_stay * 0.1)

print(f'{place_to_stay:.2f}')
