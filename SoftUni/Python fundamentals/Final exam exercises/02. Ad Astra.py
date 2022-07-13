from re import findall

data = input()
lst = findall(r"([#|/|])([a-zA-Z\s]+)\1(\d\d/\d\d/\d\d)\1(\d{1,5})\1", data)
calories = 0
for i in lst:
    calories += int(i[3])
print(f"You have food to last you for: {calories // 2000} days!")
for s in lst:
    print(f"Item: {s[1]}, Best before: {s[2]}, Nutrition: {s[3]}")
