lst = input().split(' ')
palindrome = input()
print([_ for _ in lst if _ == _[::-1]])
print(f"Found palindrome {lst.count(palindrome)} times")
