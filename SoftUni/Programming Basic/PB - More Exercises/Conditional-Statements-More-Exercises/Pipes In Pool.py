v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
p1_rabota = p1 * h
p2_rabota = p2 * h
sum_pipes = p1_rabota + p2_rabota
sum_percent_p1 = 0
sum_percent_p2 = 0
sum_percent = 0
if sum_pipes <= v:
    sum_percent = (sum_pipes / v) * 100
    sum_percent_p1 = (p1_rabota / sum_pipes) * 100
    sum_percent_p2 = (p2_rabota / sum_pipes) * 100
    print(f"The pool is {sum_percent:.2f}% full. Pipe 1: "
          f"{sum_percent_p1:.2f}%. Pipe 2: {sum_percent_p2:.2f}%.")
else:
    sum_preleli = sum_pipes - v
    print(f"For {h} hours the pool overflows"
          f" with {sum_preleli:.2f} liters.")
