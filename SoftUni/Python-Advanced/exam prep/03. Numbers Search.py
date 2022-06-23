from collections import Counter

def duplicate_nums(nums):
    counter = Counter(nums)
    asd = {k: v for k, v in counter.items() if v > 1}
    asd = asd.keys()
    return sorted(list(asd))


def missing_number(nums):
    min_num = min(nums)
    max_num = max(nums)
    for i in range(min_num, max_num):
        if i not in nums:
            return i


def numbers_searching(*args):
    lst = args
    dupl = duplicate_nums(args)
    miss_num = missing_number(lst)
    return [miss_num, dupl]



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))