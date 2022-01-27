season = input()
group_type = input()
pupils = int(input())
count_nights = int(input())

group_type1 = 0
sport = ''
if season == "Winter":
    if group_type == "boys":
        group_type1 = 9.60
        sport = 'Judo'
    elif group_type == "girls":
        group_type1 = 9.60
        sport = 'Gymnastics'
    elif group_type == "mixed":
        group_type1 = 10
        sport = 'Ski'
elif season == "Spring":
    if group_type == "boys":
        group_type1 = 7.20
        sport = 'Tennis'
    elif group_type == "girls":
        group_type1 = 7.20
        sport = 'Athletics'
    elif group_type == "mixed":
        group_type1 = 9.50
        sport = 'Cycling'
elif season == "Summer":
    if group_type == "boys":
        group_type1 = 15
        sport = 'Football'
    elif group_type == "girls":
        group_type1 = 15
        sport = 'Volleyball'
    elif group_type == "mixed":
        group_type1 = 20
        sport = 'Swimming'

sum_sum = pupils * count_nights *group_type1

if pupils >= 50:
    sum_sum -= sum_sum * 0.50
elif 20 <= pupils < 50:
    sum_sum -= sum_sum * 0.15
elif 10 <= pupils < 20:
    sum_sum -= sum_sum * 0.05

print(f'{sport} {sum_sum:.2f} lv.')
