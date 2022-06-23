from collections import deque

materials = [int(_) for _ in input().split()]
magic = deque(int(_) for _ in input().split())

dkt = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}
while magic and materials:
    mat = materials.pop()
    mag = magic.popleft()
    sum_sum = mag + mat

    if sum_sum >= 500:
        sum_sum = mat / 2 + mag / 2
    elif 99 >= sum_sum:
        flag = True
        if sum_sum % 2 == 0:
            sum_sum = mat * 2 + mag * 3
        else:
            sum_sum = mat * 2 + mag * 2

    if 499 >= sum_sum >= 400:
        dkt["Diamond Jewellery"] += 1
    elif 399 >= sum_sum >= 300:
        dkt["Gold"] += 1
    elif 299 >= sum_sum >= 200:
        dkt["Porcelain Sculpture"] += 1
    elif 199 >= sum_sum >= 100:
        dkt["Gemstone"] += 1

if (dkt["Gemstone"] >= 1 and dkt["Porcelain Sculpture"] >= 1) or (dkt['Gold'] >= 1 and dkt["Diamond Jewellery"] >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")
for k, v in sorted(dkt.items()):
    if v > 0:
        print(f"{k}: {v}")
