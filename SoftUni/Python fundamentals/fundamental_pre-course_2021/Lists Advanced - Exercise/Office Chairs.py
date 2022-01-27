rooms = int(input())
people1 = 0
chairs1 = 0
count = 0
room_people = 0
room_chairs = 0
for i in range(rooms):
    chairs, people = input().split()
    chairs1 += len(chairs)
    people1 += int(people)
    count += 1
    room_people = int(people)
    room_chairs = len(chairs)
    if room_people > room_chairs:
        sum_sum = room_people - room_chairs
        print(f"{sum_sum} more chairs needed in room {count}")
    room_people = 0
    room_chairs = 0
if chairs1 > people1:
    sum_num = chairs1 - people1
    print(f'Game On, {sum_num} free chairs left')
