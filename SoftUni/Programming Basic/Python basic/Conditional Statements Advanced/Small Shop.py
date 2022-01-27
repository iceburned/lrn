product = str(input())
town = str(input())
pieces = float(input())
if town == "Sofia":
    if product == "coffee":
        print(pieces * 0.50)
    elif product == "water":
        print(pieces * 0.80)
    elif product == "beer":
        print(pieces * 1.20)
    elif product == "sweets":
        print(pieces * 1.45)
    elif product == "peanuts":
        print(pieces * 1.60)
if town == "Plovdiv":
    if product == "coffee":
        print(pieces * 0.40)
    elif product == "water":
        print(pieces * 0.70)
    elif product == "beer":
        print(pieces * 1.15)
    elif product == "sweets":
        print(pieces * 1.30)
    elif product == "peanuts":
        print(pieces * 1.50)
if town == "Varna":
    if product == "coffee":
        print(pieces * 0.45)
    elif product == "water":
        print(pieces * 0.70)
    elif product == "beer":
        print(pieces * 1.10)
    elif product == "sweets":
        print(pieces * 1.35)
    elif product == "peanuts":
        print(pieces * 1.55)
