bottles = int(input()) * 750

pots = 0
pots_count = 0
plates = 0
plates_count = 0
loading_count = 0
sum_sum = 0
while bottles >= sum_sum:
    plates_pots = input()
    if plates_pots == "End":
        break
    plates_pots1 = int(plates_pots)
    loading_count += 1
    if loading_count == 3:
        loading_count = 0
        pots += plates_pots1 * 15
        pots_count += plates_pots1
    else:
        plates += plates_pots1 * 5
        plates_count += plates_pots1
    sum_sum = pots + plates
if bottles >= sum_sum:
    lefover = bottles - sum_sum
    print(f"Detergent was enough!\n{plates_count} dishes and {pots_count} pots were washed."
          f"\nLeftover detergent {lefover} ml.")
else:
    leftover1 = sum_sum - bottles
    print(f"Not enough detergent, {leftover1} ml. more necessary!")
