pens = int(input()) * 5.80
markers = int(input()) * 7.20
cleaner = int(input()) * 1.20
discount = int(input()) / 100

price = pens + markers + cleaner
price -= price * discount

print(price)
