from collections import deque

green_duration = int(input())
free_window = int(input())
data = input()
cars_queue = deque()
seconds_left = green_duration
car_passed = 0
flag = True
while not data == "END":
    if not data == "green":
        cars_queue.append(data)
    else:
        seconds_left = green_duration  # reset seconds
        while cars_queue:
            car_seconds = len(cars_queue[0])  # seconds for single car
            if seconds_left >= car_seconds:
                car_passed += 1
                seconds_left -= car_seconds
                cars_queue.popleft()
            elif seconds_left > 0 and seconds_left + free_window >= car_seconds:
                car_passed += 1
                cars_queue.popleft()
                free_window = free_window - seconds_left
                seconds_left = 0
            elif seconds_left == 0 and free_window >= car_seconds:
                car_passed += 1
                cars_queue.popleft()
                free_window -= car_seconds
            elif seconds_left == 0 and free_window < car_seconds:
                cars_queue.popleft()
            else:
                flag = False
                print(f"A crash happened!\n{cars_queue[0]} was hit at {cars_queue[0][seconds_left + free_window]}.")
                break
    if not flag:
        break
    data = input()
if flag:
    print(f"Everyone is safe.\n{car_passed} total cars passed the crossroads.")
