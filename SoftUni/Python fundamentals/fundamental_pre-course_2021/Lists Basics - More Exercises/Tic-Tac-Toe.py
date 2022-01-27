a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
c = [int(_) for _ in input().split()]
one = 0
two = 0
for aa in a:
    for bb in b:
        for cc in c:
            if aa == 1:
                one += 1
            elif aa == 2:
                two += 1
            if bb == 1:
                one += 1
            elif bb == 2:
                two += 1
            if cc == 1:
                one += 1
            elif cc == 2:
                two += 1
if one > two:
    print("First player won")
elif one < two:
    print("Second player won")
elif one == two:
    print("Draw!")
