from collections import deque

bomb_effect = deque(int(_) for _ in input().split(", "))
bomb_casings = deque(int(_) for _ in input().split(", "))

bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120,
}

pouch = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

while bomb_effect and bomb_casings:
    if all(True if _ >= 3 else False for _ in pouch.values()):
        break
    effect = bomb_effect.popleft()
    casing = bomb_casings.pop()
    result = effect + casing
    if result == bombs['Datura Bombs']:
        pouch['Datura Bombs'] += 1
    elif result == bombs['Cherry Bombs']:
        pouch['Cherry Bombs'] += 1
    elif result == bombs['Smoke Decoy Bombs']:
        pouch['Smoke Decoy Bombs'] += 1
    else:
        bomb_effect.appendleft(effect)
        bomb_casings.append(casing - 5)

if all(True if _ >= 3 else False for _ in pouch.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if any(bomb_effect):
    print(f"Bomb Effects: {', '.join(map(str, bomb_effect))}")
else:
    print('Bomb Effects: empty')
if any(bomb_casings):
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print('Bomb Casings: empty')

print(f"Cherry Bombs: {pouch['Cherry Bombs']}")
print(f"Datura Bombs: {pouch['Datura Bombs']}")
print(f"Smoke Decoy Bombs: {pouch['Smoke Decoy Bombs']}")
