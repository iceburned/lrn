data = [int(_) for _ in input().split(" ")]

pos = []
neg = []

for s in data:
    if s > 0:
        pos.append(s)
    else:
        neg.append(s)
pos_sum = sum(pos)
neg_sum = sum(neg)
print(neg_sum)
print(pos_sum)
if abs(pos_sum) < abs(neg_sum):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
