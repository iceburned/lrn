import math
series = input()
length_episode = int(input())
length_rest = int(input())
launch_time = length_rest * 1 / 8
rest_time = length_rest * 1 / 4
left_time = length_rest - launch_time - rest_time
diff = abs(left_time - length_episode)

if left_time >= length_episode:
    print(f'You have enough time to watch {series} and left with {math.ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(diff)} more minutes.")
