# def first(a):
#     if a == 0 or a == 1 or a == 2:
#         return 1
#     elif a == 3:
#         return 2
#     else:
#         return (first(a - 1) +
#                 first(a - 2) +
#                 first(a - 3))
#
#
# def second(a):
#     for i in range(1, a + 1):
#         print(first(i), end=' ')
#
#
# second(int(input()))


def find_tribonacci(number):
    t_nums = [1]

    num = 1
    while len(t_nums) < number:

        if len(t_nums) < 3:

            if len(t_nums) == 1:
                if num == t_nums[-1] + 0 + 0:
                    t_nums.append(num)
            elif len(t_nums) == 2:
                if num == t_nums[-1] + t_nums[-2] + 0:
                    t_nums.append(num)
        else:
            if num == t_nums[-1] + t_nums[-2] + t_nums[-3]:
                t_nums.append(num)

        num += 1

    return t_nums


def print_tribonacci(l):
    print(' '.join(map(str, l)))


num = int(input())

numlist = find_tribonacci(num)
print_tribonacci(numlist)