sequence = input().split(' ')
data = input()
moves = 0
while not data == 'end':
    if not sequence:
        break
    moves += 1
    match1, match2 = data.split(' ')
    match1 = int(match1)
    match2 = int(match2)
    if match1 == match2 or match1 < 0 or match2 < 0 or match1 > len(sequence)-1 or match2 > len(sequence)-1:
        print("Invalid input! Adding additional elements to the board")
        mid_index = len(sequence) // 2
        sequence.insert(mid_index, ('-' + str(moves) + 'a')), sequence.insert(mid_index, ('-' + str(moves) + 'a'))
    else:
        if sequence[match1] == sequence[match2]:
            print(f"Congrats! You have found matching elements - {sequence[match2]}!")
            temp_num = sequence[match2]
            for i in range(2):
                sequence.remove(temp_num)
        else:
            print("Try again!")
    data = input()
if not sequence:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(*sequence)
