price_veg = float(input())
price_fru = float(input())
total_kg_veg = int(input())
total_kg_fru = int(input())

veg = price_veg * total_kg_veg
fru = price_fru * total_kg_fru
total = veg + fru
sum_euro = total / 1.94
print(f'{sum_euro:.2f}')
