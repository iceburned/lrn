snowballs_num = int(input())
perfect_snowball = 0
weight_ball1 = 0
time_ball1 = 0
quality_ball1 = 0
for _ in range(snowballs_num):
    weight_ball = int(input())
    time_ball = int(input())
    quality_ball = int(input())
    calc_snowball = (weight_ball // time_ball) ** quality_ball
    if calc_snowball > perfect_snowball:
        perfect_snowball = calc_snowball
        weight_ball1 = weight_ball
        time_ball1 = time_ball
        quality_ball1 = quality_ball
print(f"{weight_ball1} : {time_ball1} = {perfect_snowball} ({quality_ball1})")
