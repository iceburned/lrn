mtx = [[s for s in input().split(' ')] for _ in range(int(input()))]
alice_poss = []
alice_tea = 0
for i in range(len(mtx)):
    if "A" in mtx[i]:
        poss = mtx[i].index("A")
        alice_poss.append(i)
        alice_poss.append(poss)
command = input()
flag = True
while command:

    if command == "down":
        if alice_poss[0] >= len(mtx):
            break

        if 0 <= alice_poss[0]+1 <= len(mtx)-1:
            mtx[alice_poss[0]][alice_poss[1]] = "*"
            alice_poss[0] += 1
            if mtx[alice_poss[0]][alice_poss[1]].isdigit():
                alice_tea += int(mtx[alice_poss[0]][alice_poss[1]])
                if alice_tea >= 10:
                    break
            elif mtx[alice_poss[0]][alice_poss[1]] == "R":
                mtx[alice_poss[0]][alice_poss[1]] = "*"
                flag = False
                break
            mtx[alice_poss[0]][alice_poss[1]] = "*"
        else:

            break

    elif command == "right":
        if alice_poss[1] >= len(mtx[1]):
            break
        if 0 <= alice_poss[1]+1 <= len(mtx[alice_poss[0]])-1:
            mtx[alice_poss[0]][alice_poss[1]] = "*"
            alice_poss[1] += 1
            if mtx[alice_poss[0]][alice_poss[1]].isdigit():
                alice_tea += int(mtx[alice_poss[0]][alice_poss[1]])

            elif mtx[alice_poss[0]][alice_poss[1]] == "R":
                mtx[alice_poss[0]][alice_poss[1]] = "*"
                flag = False
                break
            mtx[alice_poss[0]][alice_poss[1]] = "*"
            if alice_tea >= 10:
                break
        else:

            break

    elif command == "up":
        if alice_poss[0] == 0:
            break
        if 0 <= alice_poss[0]-1 <= len(mtx)-1:
            mtx[alice_poss[0]][alice_poss[1]] = "*"
            alice_poss[0] -= 1
            if mtx[alice_poss[0]][alice_poss[1]].isdigit():
                alice_tea += int(mtx[alice_poss[0]][alice_poss[1]])

            elif mtx[alice_poss[0]][alice_poss[1]] == "R":
                mtx[alice_poss[0]][alice_poss[1]] = "*"
                flag = False
                break
            mtx[alice_poss[0]][alice_poss[1]] = "*"
            if alice_tea >= 10:
                break
        else:

            break

    elif command == "left":
        if alice_poss[1] == 0:
            break
        if 0 <= alice_poss[1] - 1 <= len(mtx[alice_poss[0]]) - 1:
            mtx[alice_poss[0]][alice_poss[1]] = "*"
            alice_poss[1] -= 1
            if mtx[alice_poss[0]][alice_poss[1]].isdigit():
                alice_tea += int(mtx[alice_poss[0]][alice_poss[1]])

            elif mtx[alice_poss[0]][alice_poss[1]] == "R":
                mtx[alice_poss[0]][alice_poss[1]] = "*"
                flag = False
                break
            mtx[alice_poss[0]][alice_poss[1]] = "*"
            if alice_tea >= 10:
                break
        else:

            break
    command = input()

if alice_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for z in mtx:
    print(*z)
