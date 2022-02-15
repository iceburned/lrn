houses = [int(_) for _ in input().split("@")]
jumps = input()
house_index = 0
while not jumps == "Love!":
    jump, length = jumps.split(" ")
    length = int(length)
    if house_index + length >= len(houses):
        house_index = 0
        length = 0
    if houses[length + house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
        jumps = input()
        continue
    houses[length + house_index] -= 2
    house_index = length + house_index
    if houses[house_index] == 0:
        print(f"Place {house_index} has Valentine's day.")
    jumps = input()
print(f"Cupid's last position was {house_index}.")
house_count = 0
for i in houses:
    if i >= 1:
        house_count += 1
if house_count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_count} places.")
