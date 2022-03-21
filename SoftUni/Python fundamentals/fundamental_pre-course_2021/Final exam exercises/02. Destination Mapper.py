from re import finditer

data = input()
re_code = finditer(r"(?<=(\=|\/))[A-Z][A-Za-z][A-za-z]+(?=\1)", data)
points = 0
valid_destinations = [_.group() for _ in re_code]
travel_points = sum([len(_) for _ in valid_destinations])
print(f"Destinations: {', '.join(valid_destinations)}\nTravel Points: {travel_points}")
