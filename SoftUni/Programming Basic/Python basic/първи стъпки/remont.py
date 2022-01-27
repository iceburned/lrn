import math

wall_high = int(input())
wall_wide = int(input())
free_percent = int(input()) / 100
windows1 = int(input())
total_paint_area = wall_high * wall_wide * 4
total_paint_area -= total_paint_area * free_percent
total_paint_area = math.ceil(total_paint_area)

command = input()
while command != "Tired!":
    paint_liters = int(command)

    total_paint_area -= paint_liters
    if total_paint_area <= 0:
        break

    command = input()

if total_paint_area > 0:
    print(f"{total_paint_area} quadratic m left.")
elif total_paint_area == 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(total_paint_area)} l paint left!")

