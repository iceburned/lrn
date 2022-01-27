f_str = input()
s_str = input()
for i in range(len(s_str)):
    a = f_str[i]
    b = s_str[i]
    if not a == b:
        f_str = f_str.replace(a, b, 1)
        print(f_str)

# first_word = input()
# second_word = input()
# for i in range(len(first_word)):
#     if first_word[i] != second_word[i]:
#         first_word = first_word[:i] + first_word[i:i + 1].replace(first_word[i], second_word[i], 1) + first_word[i + 1:]
#         print(first_word)
