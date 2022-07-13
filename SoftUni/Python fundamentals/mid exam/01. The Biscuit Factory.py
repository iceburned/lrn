import math


biscuits_per_day = int(input())
workers = int(input())
biscuits_per_month = int(input())
total_biscuits = 0
for i in range(1, 31):
    if i % 3 == 0:
        total_biscuits += int(biscuits_per_day * 0.75 * workers)
    else:
        total_biscuits += biscuits_per_day * workers
biscuits = math.floor(total_biscuits)
biscuits1 = abs(biscuits - biscuits_per_month)
print(f"You have produced {biscuits} biscuits for the past month.")
percentage = biscuits1 / biscuits_per_month * 100
if biscuits > biscuits_per_month:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
