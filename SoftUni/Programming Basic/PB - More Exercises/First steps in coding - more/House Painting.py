x = float(input())
y = float(input())
h = float(input())

# steni
s_square = (2 * x**2) - (1.2 * 2)
s_rectangle = (2 * (x * y)) - (2 * 1.5**2)
walls = s_rectangle + s_square
paint_green = walls / 3.4
print(f'{paint_green:.2f}')
#tavan
s_square_roof = 2 * (x * y)
s_triangle_roof = 2 * ((x * h) / 2)
roof = s_triangle_roof + s_square_roof
paint_red = roof / 4.3
print(f'{paint_red:.2f}')
