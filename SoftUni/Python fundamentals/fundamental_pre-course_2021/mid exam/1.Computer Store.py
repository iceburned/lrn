data = input()
total_sum = 0
taxes = 0
while not data == "special" and not data == "regular":
    data = float(data)
    if data > 0:
        total_sum += data
        taxes += data * 0.20
    elif data == 0:
        print("Invalid order!")
    elif data < 0:
        print("Invalid price!")
    data = input()
sum_with_taxes = total_sum + taxes
if sum_with_taxes == 0:
    print("Invalid order!")
elif data == "special":
    sum_with_taxes -= sum_with_taxes * 0.10
    print(f"Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {total_sum:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {sum_with_taxes:.2f}$")
else:
    print(f"Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {total_sum:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {sum_with_taxes:.2f}$")
