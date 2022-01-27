import math

w = float(input()) * 100
h = float(input()) * 100
h1 = h - 100
table_row = math.floor(h1 / 70)
room_length = math.floor(w / 120)
places = table_row * room_length - 3
print(places)
