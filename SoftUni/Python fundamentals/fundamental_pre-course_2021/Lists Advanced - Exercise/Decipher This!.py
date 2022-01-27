lst = input().split(' ')
for i in lst:
    char = ''
    is_digit = ''.join(filter(str.isdigit, i))
    is_letter = ''.join(filter(str.isalpha, i))
    first_letter = is_letter[0]
    if len(is_letter) == 1:
        print(chr(int(is_digit)) + first_letter, end=' ')
    else:
        last_letter = is_letter[-1]
        swapped_str = last_letter + is_letter[1:-1] + first_letter
        print(chr(int(is_digit)) + swapped_str, end=' ')


# друга идея за смяна на букви
#
# new_word[1], new_word[-1] = new_word[-1], new_word[1]