import re

data = sorted([_.strip() for _ in input().split(",")])
for code in data:
    regex_health = re.findall(r"[^0-9\+\-\*\/\.]", code)
    health = 0
    for i in regex_health:
        health += ord(i)
    regex_damage = re.finditer(r"(\+|\-)?[\d+\.\d+]+|[\d+]", code)
    damage = 0
    for s in regex_damage:
        damage += float((s.group()))
    for zz in code:
        if zz == "*":
            damage *= 2
        elif zz == "/":
            damage /= 2
    print(f"{code} - {health} health, {damage:.2f} damage")

