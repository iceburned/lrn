data = input().strip().split()
sum_sum = []
dict_lower = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
dict_upper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
for s in data:
    letters = ''
    digit = ''
    for ss in s:
        if ss.isdigit():
            digit += ''.join(ss)
        else:
            letters += ''.join(ss)
    digit = int(digit)
    frst_letter = letters[:1]
    lst_letter = letters[-1]
    temp_sum = 0
    if frst_letter.isupper():
        temp_sum = digit / dict_upper[frst_letter]
    else:
        temp_sum = digit * dict_lower[frst_letter]
    if lst_letter.isupper():
        sum_sum.append(temp_sum - dict_upper[lst_letter])
    else:
        sum_sum.append(temp_sum + dict_lower[lst_letter])
print(f"{sum(sum_sum):.2f}")
