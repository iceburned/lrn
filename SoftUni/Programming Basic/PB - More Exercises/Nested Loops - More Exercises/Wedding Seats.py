last_sector = input()
rows = int(input())
seats = int(input())
a1 = ''
rows_count = 0
seats_sum = 0
seat_count = 0
seat_count1 = ''
for a in range(ord('A'), ord(last_sector) + 1):
    rows_count += 1
    for b in range(1, rows + rows_count):
        a1 = chr(a)
        seat_count1 = ord('a')
        if b % 2 == 0:
            seat_count += seats + 2
        else:
            seat_count = seats
        for c in range(1, seat_count + 1):
            print(f'{a1}{b}{chr(seat_count1)}')
            seats_sum += 1
            seat_count1 += 1
        seat_count = 0
print(seats_sum)
