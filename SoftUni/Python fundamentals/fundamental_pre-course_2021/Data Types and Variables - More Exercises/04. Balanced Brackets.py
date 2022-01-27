lines = int(input())
str_letter = ''
flag = False
# open_bracket = False
for i in range(lines):
    data = input()
    str_letter += ''.join(data)
a = str_letter.count('(')
b = str_letter.count(')')
if a == b:
    print('BALANCED')
else:
    print('UNBALANCED')

# n = int(input())
# times1 = 0
# times2 = 0
# is_open = False
# is_break = False
# for c in range(1, n + 1):
#     symbol = input()
#     if symbol == "(":
#         is_open = True
#         times1 += 1
#         times2 = 0
#         if times1 == 2:
#             is_break = True
#             break
#     elif symbol == ")":
#         times2 += 1
#         if times2 == 2:
#             is_break = True
#             break
#         if is_open:
#             is_open = False
#             times1 = 0
# if is_break:
#     print("UNBALANCED")
# else:
#     print("BALANCED")
