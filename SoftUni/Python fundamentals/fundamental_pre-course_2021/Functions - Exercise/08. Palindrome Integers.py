def palindrome(num):
    for i in num:
        if i == i[::-1]:
            print('True')
        else:
            print('False')


nums = [_ for _ in input().split(', ')]
palindrome(nums)
