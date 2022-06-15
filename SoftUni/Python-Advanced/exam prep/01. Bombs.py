from collections import deque

bomb_effect = deque(int(_) for _ in input().split(", "))
bomb_casings = [int(_) for _ in input().split(", ")]

lst = [0, 0, 0]
while bomb_effect and bomb_casings:
    if all([True if (_ >= 3) else False for _ in lst]):
        break
    effect = bomb_effect.popleft()
    casing = bomb_casings.pop()
    if effect + casing == 120:
        lst[0] += 1
    elif effect + casing == 60:
        lst[1] += 1
    elif effect + casing == 40:
        lst[2] += 1
    else:
        bomb_effect.appendleft(effect)
        bomb_casings.append(casing - 5)

if all([True if (_ >= 3) else False for _ in lst]):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
print(f"Bomb Effects: {', '.join(map(str, bomb_effect)) if any(bomb_effect) else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings)) if any(bomb_casings) else 'empty'}")
print(f"Cherry Bombs: {lst[1]}\nDatura Bombs: {lst[2]}\nSmoke Decoy Bombs: {lst[0]}")
