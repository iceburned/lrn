# rooms = int(input())
# people1 = 0
# chairs1 = 0
# count = 0
# for i in range(rooms):
#     chairs, people = input().split()
#     chairs1 += len(chairs)
#     people1 += int(people)
#     count += 1
#     room_people = int(people)
#     room_chairs = len(chairs)
#     if room_people > room_chairs:
#         sum_sum = room_people - room_chairs
#         print(f"{sum_sum} more chairs needed in room {count}")
# if chairs1 > people1:
#     sum_num = chairs1 - people1
#     print(f'Game On, {sum_num} free chairs left')
#

rooms_count = int(input())

total_free_chairs = 0
is_enough = True
for room in range(1, rooms_count + 1):
	room_condition = input().split()
	chairs_count = len(room_condition[0])
	chairs_taken = int(room_condition[1])
	free_chairs = chairs_count - chairs_taken
	if free_chairs < 0:
		is_enough = False
		chairs_needed = abs(free_chairs)
		print(f"{chairs_needed} more chairs needed in room {room}")
	else:
		total_free_chairs += free_chairs

if is_enough:
	print(f"Game On, {total_free_chairs} free chairs left")