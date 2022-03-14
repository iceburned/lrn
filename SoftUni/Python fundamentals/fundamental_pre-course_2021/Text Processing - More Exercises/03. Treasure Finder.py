# import re
#
# decrypt = [int(_) for _ in input().split(" ")]
# data = input()
# new_string = ''
# while not data == "find":
#     index = 0
#     for i in data:
#         new_string += "".join(chr(ord(i) - decrypt[index]))
#         index += 1
#         if index >= 4:
#             index = 0
#     material = re.findall(r'&(\w+)&', new_string)
#     position = re.findall(r'<(\w+)>', new_string)
#     print(f"Found {material[0]} at {position[0]}")
#     new_string = ''
#     data = input()
