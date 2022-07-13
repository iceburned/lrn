# def take_skip_opperations(take_list, skip_list, non_nums):
#     words = ''
#     for i in range(len(take_list)):
#         take = take_list[i]
#         for a in range(0, take):
#             if len(non_nums) > a:
#                 words += ''.join(non_nums[a])
#         for a in range(0, take):
#             if len(non_nums) > a:
#                 non_nums.pop(0)
#         skip = skip_list[i]
#         for b in range(0, skip):
#             if len(non_nums) > b:
#                 non_nums.pop(0)
#     return words
#
#
# def separate(str_input):
#     nums = []
#     non_nums = []
#     [nums.append(_) if _.isdigit() else non_nums.append(_) for _ in str_input]
#     return nums, non_nums
#
#
# def split_nums(nums):
#     nums = [int(_) for _ in nums]
#     take_list = []
#     skip_list = []
#     [take_list.append(nums[_]) if _ % 2 == 0 else skip_list.append(nums[_]) for _ in range(len(nums))]
#     return take_list, skip_list
#
#
# str_input = input()
# nums, non_nums = separate(str_input)
# take_list, skip_list = split_nums(nums)
# answer = take_skip_opperations(take_list, skip_list, non_nums)
# print(answer)


str_input = input()
num_list = [int(x) for x in str_input if x.isnumeric()]
take_list = [num_list[i] for i in range(len(num_list)) if i % 2 == 0]
skip_list = [num_list[i] for i in range(len(num_list)) if i % 2 != 0]

letter_list = [x for x in str_input if not x.isnumeric()]

output = ''

for i in range(len(take_list)):
    output += ''.join((letter_list[:take_list[i]]))
    letter_list = letter_list[take_list[i] + skip_list[i]:]

print(output)