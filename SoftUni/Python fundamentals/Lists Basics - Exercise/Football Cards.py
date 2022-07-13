import sys

data_inp = input()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lst = data_inp.split(' ')
for i in lst:
    if len(a) < 7 or len(b) < 7:
        print(f'Team A - {len(a)}; Team B - {len(b)}\nGame was terminated')
        sys.exit()

    if 'A' in i:
        num = i.replace('A-', '')
        num = int(num)
        for n in a:
            if n == num:
                a.remove(num)
    elif 'B' in i:
        num1 = i.replace('B-', '')
        num1 = int(num1)
        for n1 in b:
            if n1 == num1:
                b.remove(num1)
print(f'Team A - {len(a)}; Team B - {len(b)}')

#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# card_input = input().split()
# terminated = False
# for card in card_input:
#     card_info = card.split('-')
#     team_name = card_info[0]
#     player_number = card_info[1]
#     if team_name == 'A' and player_number in a:
#         a.remove(player_number)
#     elif team_name == 'B' and player_number in b:
#         b.remove(player_number)
#     if len(a) < 7 or len(b) < 7:
#         terminated = True
#         break
# print(f'Team A - {len(a)}; Team B - {len(b)}')
# if terminated:
#     print(f'Team A - {len(a)}; Team B - {len(b)}\nGame was terminated')
