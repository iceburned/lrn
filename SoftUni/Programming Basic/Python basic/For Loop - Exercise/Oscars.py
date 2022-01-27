actor_name = str(input())
academy_points = float(input())
judges = int(input())

bonus = 0
judge_sum = 0

for _ in range(judges):
    if _ == 0:
        judge_sum = academy_points
    judge_name = str(input())
    judge_points = float(input())
    judge_sum += ((len(judge_name) * judge_points) / 2)
    if judge_sum >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {judge_sum:.1f}!")
        break
if judge_sum < 1250.5:
    sum_sum = 1250.5 - judge_sum
    print(f"Sorry, {actor_name} you need {sum_sum:.1f} more!")
