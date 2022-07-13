a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
c = [int(_) for _ in input().split()]
winner = 0
is_winner = False

# rows
if a[0] == b[0] == c[0] != 0:
    is_winner = True
    winner = a[0]
elif a[1] == b[1] == c[1] != 0:
    is_winner = True
    winner = a[1]
elif a[2] == b[2] == c[2] != 0:
    is_winner = True
    winner = a[2]

# check columns
if a[0] == a[1] == a[2] != 0:
    is_winner = True
    winner = a[0]
elif b[0] == b[1] == b[2] != 0:
    is_winner = True
    winner = b[0]
elif c[0] == c[1] == c[2] != 0:
    is_winner = True
    winner = c[0]

if a[0] == b[1] == c[2] != 0:
    is_winner = True
    winner = a[0]
elif a[2] == b[1] == c[0] != 0:
    is_winner = True
    winner = a[2]

if winner == 1 and is_winner:
    print("First player won")
elif winner == 2 and is_winner:
    print("Second player won")
else:
    print("Draw!")
