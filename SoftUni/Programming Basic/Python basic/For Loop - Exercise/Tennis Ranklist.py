import math

tournament = int(input())
starting_points = int(input())

points = 0
points1 = 0
wins = 0
for _ in range(tournament):
    tournament_stage = str(input())
    if _ == 0:
        points += starting_points
    if tournament_stage == "W":
        wins += 1
    if tournament_stage == "F":
        points += 1200
        points1 += 1200
    elif tournament_stage == "W":
        points += 2000
        points1 += 2000
    elif tournament_stage == "SF":
        points += 720
        points1 += 720


average_points = points1 / tournament
wins_tournaments = wins / tournament * 100

print(f"Final points: {points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{wins_tournaments:.2f}%")
