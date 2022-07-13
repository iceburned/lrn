lst = list(map(int, input().split(', ')))
lst = [int(_) for _ in lst]
positive = []
[positive.append(str(_)) for _ in lst if _ >= 0]
print('Positive: ' + ', '.join(positive))
negative = []
[negative.append(str(_)) for _ in lst if _ < 0]
print('Negative: ' + ', '.join(negative))
even = []
[even.append(str(_)) for _ in lst if _ % 2 == 0]
print('Even: ' + ', '.join(even))
odd = []
[odd.append(str(_)) for _ in lst if not _ % 2 == 0]
print('Odd: ' + ', '.join(odd))


# second answer
numbers = list(map(int, input().split(', ')))
positives, negatives, evens, odds = [], [], [], []
for x in numbers:
    positives.append(str(x)) if x >= 0 else negatives.append(str(x))
    evens.append(str(x)) if x % 2 == 0 else odds.append(str(x))

print(f"Positives: {', '.join(positives)}")
print(f"Negatives: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odds: {', '.join(odds)}")
