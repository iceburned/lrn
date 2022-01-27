data = input()
while not data == "end":
    print(data, end=' ')
    print("= " + data[::-1])
    data = input()


# data = input()
# while not data == "end":
#     print(data, end=' ')
#     a_list = list(data)
#     a_list.reverse()
#     print('= ' + ''.join(a_list))
#     data = input()


# data = input()
# reversed_string = ''
# while not data == "end":
#     print(data, end=' ')
#     for i in data:
#         reversed_string = i + reversed_string
#     print('= ' + reversed_string)
#     reversed_string = ''
#     data = input()


# data = input()
# reversed_string = ''
# i = len(data) -1
# while not data == "end":
#     print(data, end=' ')
#     while i >= 0:
#         reversed_string += data[i]
#         i -= 1
#     print("= " + reversed_string)
#     data = input()
#     i = len(data)-1
#     reversed_string = ''

