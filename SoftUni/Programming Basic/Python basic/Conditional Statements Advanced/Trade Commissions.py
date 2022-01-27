town = str(input())
sell = float(input())
sell1 = 0

if 0 <= sell <= 500:
    if town == "Sofia":
        sell1 = (sell * 0.050)
    elif town == "Varna":
        sell1 = (sell * 0.045)
    elif town == "Plovdiv":
        sell1 = (sell * 0.055)
    else:
        print("error")
elif 500 <= sell <= 1000:
    if town == "Sofia":
        sell1 = (sell * 0.070)
    elif town == "Varna":
        sell1 = (sell * 0.075)
    elif town == "Plovdiv":
        sell1 = (sell * 0.080)
    else:
        print("error")
elif 1000 <= sell <= 10000:
    if town == "Sofia":
        sell1 = (sell * 0.080)
    elif town == "Varna":
        sell1 = (sell * 0.10)
    elif town == "Plovdiv":
        sell1 = (sell * 0.12)
    else:
        print("error")
elif sell >= 10000:
    if town == "Sofia":
        sell1 = (sell * 0.12)
    elif town == "Varna":
        sell1 = (sell * 0.13)
    elif town == "Plovdiv":
        sell1 = (sell * 0.145)
    else:
        print("error")
else:
    print("error")
if sell1 != 0:
    print(f'{sell1:.2f}')
