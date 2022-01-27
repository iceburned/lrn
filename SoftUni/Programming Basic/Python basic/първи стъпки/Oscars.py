actor_name = input()
actor_point = float(input())
n = int(input())


for i in range(n):
    grader_name = input()
    grader_points = float(input())

    grader_total_points = (len(grader_name) * grader_points) / 2
    actor_point += grader_total_points

    if actor_point > 1250.5:
        break

if actor_point >1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_point:.1f}!")
else:
    points_needed = 1250.5 - actor_point
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")
