houses = [int(_) for _ in input().split("@")]
jumps = input()
house_index = 0
while not jumps == "Love!":
    jump, length = jumps.split(" ")
    length = int(length)
    if house_index + length < len(houses):
        house_index += length
    else:
        house_index = 0
    if houses[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        houses[house_index] -= 2
        if houses[house_index] <= 0:
            print(f"Place {house_index} has Valentine's day.")
    jumps = input()
print(f"Cupid's last position was {house_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([h for h in houses if h!=0])} places.")
