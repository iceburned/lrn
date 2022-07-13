a = input().split(', ')
count = 0
for i in a[::-1]:
    if a[-1] == 'wolf' and count == 0:
        print('Please go away and stop eating my sheep')
        break
    else:
        if i == 'wolf':
            print(f'Oi! Sheep number {count}! You are about to be eaten by a wolf!')
        else:
            if a[-1] == 'sheep':
                count += 1
                a.pop()
