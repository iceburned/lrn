data = input()
dkt = {}
while not data == "buy":
    product, single_price, count = data.split(" ")
    single_price = float(single_price)
    count = int(count)
    if product not in dkt:
        dkt[product] = [single_price, count]
    else:
        dkt[product][1] += count
        if single_price != dkt[product][0]:
            dkt[product][0] = single_price
    data = input()
for key, value in dkt.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")
