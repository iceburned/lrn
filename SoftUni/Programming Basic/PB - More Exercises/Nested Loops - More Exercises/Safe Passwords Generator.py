a = int(input())
b = int(input())
max1 = int(input())
count = 0
A = 34
B = 63

for x in range(1, a + 1):
    for y in range(1, b + 1):
        A += 1
        B += 1
        if A > 55:
            A = 35
        if B > 96:
            B = 64
        count += 1
        if count > max1:
            break
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
