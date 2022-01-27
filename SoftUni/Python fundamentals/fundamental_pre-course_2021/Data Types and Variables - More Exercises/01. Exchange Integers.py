a = int(input())
b = int(input())
print(f'Before: \na = {a}\nb = {b}')
y = a
z = b
a = z
b = y
print(f'After:\na = {a}\nb = {b}')
