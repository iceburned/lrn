groups_count = int(input())

sum_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
for _ in range(groups_count):
    people_in_group = int(input())
    sum_people += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimandjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

musala_sum = musala / sum_people * 100
monblan_sum = monblan / sum_people * 100
kilimandjaro_sum = kilimandjaro / sum_people * 100
k2_sum = k2 / sum_people * 100
everest_sum = everest / sum_people * 100

print(f'{musala_sum:.2f}%\n{monblan_sum:.2f}%\n{kilimandjaro_sum:.2f}%\n{k2_sum:.2f}%\n'
      f'{everest_sum:.2f}%')
